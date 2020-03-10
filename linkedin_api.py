from linkedin import Linkedin
import pickle
import json

# Authenticate using any Linkedin account credentials
api = Linkedin('', '')

# GET a profile
profile3 = api.get_profile('sumitdarak')
print(profile1)
profile_urn_id1 = profile1['profile_id']

# GET a profiles contact info
contact_info1 = api.get_profile_contact_info('sumitdarak')
print(contact_info1)


profile_info1 = api.get_profile_skills('sumitdarak')
print(profile_info1)

# GET all connected profiles (1st, 2nd and 3rd degree) of a given profile
connections1 = api.get_profile_connections('sumitdarak')
print(connections1)

darak={}

darak['name']=profile1['firstName']+" "+profile1['lastName']

for edc in profile1['education']:
    temp=edc['timePeriod']
    time=""
    for t in temp:
        #print(temp[t]['year'])
        time=str(temp[t]['year'])+" "+time
    edc['timePeriod']=time
print(profile1['education'])

darak['education']=profile1['education']


darak['experience']=profile1['experience']

darak['headline']=profile1['headline']

darak['geo']=profile1['geoLocationName']     

darak['contact']=contact_info1

inf=[]
for info in profile_info1:
    inf.append(info['name'])

darak['skills']=inf

connect={}
counter=0
for con in connections1:
    counter+=1
    connect[counter]={}
    connect[counter]['public_id']=con['public_id']
    connect[counter]['urn_id']=con['urn_id']

darak['coonections']=connect

print(darak['coonections'])

darak=json.dumps(darak)
pickle.dump(darak,open("darak_linkedin.pkl","wb"))
#######################################################################################
# GET a profile
profile = api.get_profile('bijendra-jain-9055973a')
print(profile)
profile_urn_id = profile['profile_id']

# GET a profiles contact info
contact_info = api.get_profile_contact_info('bijendra-jain-9055973a')
print(contact_info)


profile_info = api.get_profile_skills('bijendra-jain-9055973a')
print(profile_info)

# GET all connected profiles (1st, 2nd and 3rd degree) of a given profile
connections = api.get_profile_connections('bijendra-jain-9055973a')
print(connections)

jain={}

jain['name']=profile['firstName']+" "+profile['lastName']

for edc in profile['education']:
    temp=edc['timePeriod']
    time=""
    for t in temp:
        #print(temp[t]['year'])
        time=str(temp[t]['year'])+" "+time
    edc['timePeriod']=time
print(profile['education'])

jain['education']=profile['education']


jain['experience']=profile['experience']

jain['headline']=profile['headline']

jain['geo']=profile['geoLocationName']     

jain['contact']=contact_info

inf=[]
for info in profile_info:
    inf.append(info['name'])

jain['skills']=inf
print(jain['skills'])
connect={}
counter=0
for con in connections:
    counter+=1
    connect[counter]={}
    connect[counter]['public_id']=con['public_id']
    connect[counter]['urn_id']=con['urn_id']

jain['coonections']=connect

print(jain['coonections'])

jain=json.dumps(jain)
pickle.dump(jain,open("jain_linkedin.pkl","wb"))
#######################################################################################
# GET a profile
profile3 = api.get_profile('rajivratn')
print(profile3)
profile_urn_id3 = profile3['profile_id']

# GET a profiles contact info
contact_info3 = api.get_profile_contact_info('rajivratn')
print(contact_info3)


profile_info3 = api.get_profile_skills('rajivratn')
print(profile_info3)

# GET all connected profiles (1st, 2nd and 3rd degree) of a given profile
connections3 = api.get_profile_connections('rajivratn')
print(connections3)

#############################################
shah={}

shah['name']=profile3['firstName']+" "+profile3['lastName']

for edc in profile3['education']:
    temp=edc['timePeriod']
    time=""
    for t in temp:
        #print(temp[t]['year'])
        time=str(temp[t]['year'])+" "+time
    edc['timePeriod']=time
print(profile3['education'])

shah['education']=profile3['education']


shah['experience']=profile3['experience']

shah['headline']=profile3['headline']

shah['geo']=profile3['geoLocationName']     
print(shah)
shah['contact']=contact_info3

inf=[]
for info in profile_info3:
    inf.append(info['name'])

shah['skills']=inf

connect={}
counter=0
for con in connections3:
    counter+=1
    connect[counter]={}
    connect[counter]['public_id']=con['public_id']
    connect[counter]['urn_id']=con['urn_id']

shah['coonections']=connect

print(shah['coonections'])
shah=json.dumps(shah)
pickle.dump(shah,open("shah_linkedin.pkl","wb"))

x=pickle.load(open("darak_linkedin.pkl","rb"))
x=json.loads(x)

print(x['contact'])



