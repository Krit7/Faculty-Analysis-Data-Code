import tweepy
import pickle
import datetime
import time
import plotly.graph_objects as go
import operator
from opencage.geocoder import OpenCageGeocode
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
from plotly.offline import plot
from bokeh.models import HoverTool
from bokeh.plotting import figure, save
from bokeh.models import ColumnDataSource
from bokeh.plotting import output_file
from bokeh.plotting import figure, show, output_file
from bokeh.tile_providers import get_provider, Vendors
from bokeh.models import ColumnDataSource
import pandas as pd
    
key=""

auth = tweepy.OAuthHandler('','')
auth.set_access_token('', '')
api = tweepy.API(auth)
if (not api):
    print("Authentication failed :(")
else:
    print("Authentication successfull!!! :D")
    
#-----------------------------------------Collection of Tweets-------------------------------------------------------------------------
NAME='@midasIIITD'
user=api.get_user(NAME)

last_tweet_date=datetime.datetime(2020,2,28)
first_tweet_date=datetime.datetime(2009,2,27)

tweets=[]
no_of_days=420
curr=time.time()
for tweet in tweepy.Cursor(api.user_timeline,id=user.id,tweet_mode="extended").items():
    
    tweets.append(tweet)

end=time.time()
print("Time taken to fetch the tweets: {0:.2f}".format(end-curr))
print('Total number of tweets', len(tweets))
print('No of days', no_of_days)

pickle.dump(tweets,open("C:/Users/Jatin/Desktop/MidsemHack/midas_tweets.pkl", "wb"))

#--------------------------------------------Collection of followers----------------------------------------------------------------------

user_followers=[]
user=api.get_user('@Sum_D')
cursor=tweepy.Cursor(api.followers,id=user.id,count=200).items()
while True:
    try:
        follower=cursor.next()
        user_followers.append(follower)
    except tweepy.RateLimitError:
        print("Tweepy Rate Limit Error")
        break
print('No of followers fetched:',len(user_followers))

pickle.dump(user_followers,open("C:/Users/Jatin/Desktop/MidsemHack/darak_followers.pkl", "wb"))

user_followers=pickle.load(open("C:/Users/Jatin/Desktop/MidsemHack/darak_followers.pkl","rb"))

lat=[]
long=[]
geocoder = OpenCageGeocode(key)
name=[]
counter=0
for user in user_followers:
    print(counter)
    loaction= geocoder.geocode(user.location)
    if len(loaction)!=0:
        lat.append(loaction[0]['geometry']['lat'])
        long.append(loaction[0]['geometry']['lng'])
        name.append(user.screen_name)
        print(counter,name[counter],lat[counter],long[counter])
        counter+=1

coordinates=(name,lat,long)
pickle.dump(coordinates,open("C:/Users/Jatin/Desktop/MidsemHack/darak_followers_location.pkl", "wb"))

####################################################################################33
coordinates=pickle.load(open("C:/Users/Jatin/Desktop/MidsemHack/shah_followers_location.pkl","rb"))

def getPointCoords(row, geom, coord_type):
    """Calculates coordinates ('x' or 'y') of a Point geometry"""
    if coord_type == 'x':
        return row[geom].x
    elif coord_type == 'y':
        return row[geom].y

def map(df1,df2,df3):
    tile_provider = get_provider(Vendors.CARTODBPOSITRON)
    
    psource1 = ColumnDataSource(df1)
    psource2 = ColumnDataSource(df2)
    psource3 = ColumnDataSource(df3)
    # range bounds supplied in web mercator coordinates
    Tooltips = [('username', '@name')]
    p = figure(x_range=(-2000000, 6000000), y_range=(-1000000, 7000000),x_axis_type="mercator", y_axis_type="mercator",tooltips=Tooltips)
    p.title.text = 'Geotagged followers from twitter (Click on faculty name)'
    p.add_tile(tile_provider)
    
    p.circle(x='long', y='lat', size=9, color="color",alpha=0.7,legend_label="BN Jain", source=psource1)
    p.square(x='long', y='lat', size=7, color="color",alpha=0.7,legend_label="Sumit Darak", source=psource2)
    p.asterisk(x='long', y='lat', size=8, color="color",alpha=0.7,legend_label="Rajiv Ratn", source=psource3)
    
    p.legend.location = "top_left"
    p.legend.click_policy="hide"
    outfp = r"C:/Users/Jatin/Desktop/points.html"
    save(obj=p, filename=outfp)
    show(p)

lat=coordinates[1]
long=coordinates[2]
geometry = [Point(xy) for xy in zip(long,lat)]
gdf = GeoDataFrame(geometry=geometry)
gdf['long'] = gdf.apply(getPointCoords, geom='geometry', coord_type='x', axis=1)
gdf['lat'] = gdf.apply(getPointCoords, geom='geometry', coord_type='y', axis=1)
gdf = gdf.drop('geometry', axis=1).copy()
gdf['name']=coordinates[0]
gdf['color']="red"
gdf['faculty']="Rajiv Ratn"


k = 6378137
gdf["long"] = gdf["long"] * (k * np.pi/180.0)
gdf["lat"] = np.log(np.tan((90 + gdf["lat"]) * np.pi/360.0)) * k
gdf.head()

df1=gdf
df2=gdf
df3=gdf

pickle.dump((df1,df2,df3),open("C:/Users/Jatin/Desktop/MidsemHack/location_dataframes.pkl", "wb"))
(df1,df2,df3)=pickle.load(open("C:/Users/Jatin/Desktop/MidsemHack/location_dataframes.pkl", "rb"))
map(df1,df2,df3)



#--------------------------------------------retweeters----------------------------------------------------------------------
tweets=pickle.load(open("midas_tweets.pkl","rb"))
retweeters={}
retweets=[]
for tweet in tweets:
    try: 
        for retweet in api.retweets(tweet.id,100):
            retweets.append(retweet)
            user_name=retweet.user.screen_name
            if user_name in retweeters.keys():
                retweeters[user_name]+=1
            else:
                retweeters[user_name]=1
    except tweepy.RateLimitError:
        print("Tweepy Rate Limit Error")
        break
    
pickle.dump(retweets,open("midas_retweets.pkl", "wb"))
pickle.dump(retweeters,open("midas_retweeters_freq.pkl", "wb"))

sorted_retweeters = sorted(retweeters.items(), key=operator.itemgetter(1),reverse=True) 
Top_10=sorted_retweeters[:10]
Top_10_Profiles=[0]*10
for i in range(10):
    Top_10_Profiles[i]=Top_10[i][0]


retweets_by_Top_10=[]
for retweet in retweets:
    if retweet.user.screen_name in Top_10_Profiles:
            retweets_by_Top_10.append(retweet)

#tweet_hours={'00':0,'01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0,'13':0,'14':0,'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'21':0,'22':0,'23':0}
#tweet_days={'01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0,'13':0,'14':0,'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'21':0,'22':0,'23':0,'24':0,'25':0,'26':0,'27':0,'28':0,'29':0,'30':0,'31':0}
tweet_months={'Jan':0,'Feb':0,'Mar':0,'Apr':0,'May':0,'Jun':0,'Jul':0,'Aug':0,'Sep':0,'Oct':0,'Nov':0,'Dec':0}

for tweet in retweets:
    tweet_created=tweet._json['created_at']
    tweet_months[tweet_created[4:7]]+=1
    
x=[]
y=[]
for a,b in tweet_months.items():
    x.append(a)
    y.append(b)

scatter_graph=go.Scatter(x=x,y=y,mode='markers',marker_color=y,text='Month, No. of Tweets')
fig = go.Figure(scatter_graph)
fig.update_layout(title='RT Freq of Top 10 followers of midasIIITD w.r.t Months')
plot(fig)

Top_10_rtno=[0]*10
for i in range(10):
    Top_10_rtno[i]=Top_10[i][1]
fig = go.Figure([go.Bar(x=Top_10_Profiles,y= Top_10_rtno)])
fig.update_layout(title='No of Retweets by Top 10 followers of midasIIITD')
plot(fig)
=============================================================================
# =============================================================================
# retweets=pickle.load(open("shah_retweets.pkl","rb"))
# retweeters=pickle.load(open("shah_retweeters_freq.pkl","rb"))
# =============================================================================
 =============================================================================
