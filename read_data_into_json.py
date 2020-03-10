
shah={}
shah[1]={}
i=1
with open("shah.txt","r") as f:
    for line in f:
        if len(line)==1:
            i+=1
            shah[i]={}
                        
        elif len(line)>1:
            print("###########################")
            print(len(line))
            words=line.split()
            head=words[0]
            y=line.split(head,1)[1]
            point=y.rfind("\n")
            if head =="Title":
                shah[i][head]=y[:point]
                print(head,words[1])
            elif (head=="URL" or head=="Year" or head=="Citations" or head=="Versions") and words[1]!="list":
                shah[i][head]=words[1]
                print(head,words[1])
            elif head=="Cluster":
                shah[i][head+" ID"]=words[2]
                print(head,words[2])
            elif (head=="Citations" or head=="Versions") and words[1]=="list":
                temp=words[2]
                x=temp.rfind(",")
                shah[i][head+" list"]=temp[:x]
                print(head,temp[:x])
f.close()
print(shah)


darak={}
darak[1]={}
i=1
with open("darak.txt","r") as f:
    for line in f:
        if len(line)==1:
            i+=1
            darak[i]={}
                        
        elif len(line)>1:
            print("###########################")
            print(len(line))
            words=line.split()
            head=words[0]
            y=line.split(head,1)[1]
            point=y.rfind("\n")
            if head =="Title":
                darak[i][head]=y[:point]
                print(head,words[1])
            elif (head=="URL" or head=="Year" or head=="Citations" or head=="Versions") and words[1]!="list":
                darak[i][head]=words[1]
                print(head,words[1])
            elif head=="Cluster":
                darak[i][head+" ID"]=words[2]
                print(head,words[2])
            elif (head=="Citations" or head=="Versions") and words[1]=="list":
                temp=words[2]
                x=temp.rfind(",")
                darak[i][head+" list"]=temp[:x]
                print(head,temp[:x])
f.close()
print(darak)


jain={}
jain[1]={}
i=1
with open("jain.txt","r") as f:
    for line in f:
        if len(line)==1:
            i+=1
            jain[i]={}
                        
        elif len(line)>1:
            print("###########################")
            print(len(line))
            words=line.split()
            head=words[0]
            y=line.split(head,1)[1]
            point=y.rfind("\n")
            if head =="Title":
                jain[i][head]=y[:point]
                print(head,words[1])
            elif (head=="URL" or head=="Year" or head=="Citations" or head=="Versions") and words[1]!="list":
                jain[i][head]=words[1]
                print(head,words[1])
            elif head=="Cluster":
                jain[i][head+" ID"]=words[2]
                print(head,words[2])
            elif (head=="Citations" or head=="Versions") and words[1]=="list":
                temp=words[2]
                x=temp.rfind(",")
                jain[i][head+" list"]=temp[:x]
                print(head,temp[:x])
f.close()
print(jain)
    

del shah[11]
del darak[11]
del jain[11]
print(shah)
print(darak)
print(jain)

import json
shah=json.dumps(shah)
darak=json.dumps(darak)
jain=json.dumps(jain)


import pickle
pickle.dump(shah,open("shah_json.pkl","wb"))
pickle.dump(darak,open("darak_json.pkl","wb"))
pickle.dump(jain,open("jain_json.pkl","wb"))

x=pickle.load(open("shah_json.pkl","rb"))
x=json.loads(x)
print(x)
