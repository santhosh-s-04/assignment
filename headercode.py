import os
import sys
import json

global d
d={}

class crd():
        
    def path(z):
        if(z!=1 and z!=2):
            print("enter valid input")
        else:
            if(z==2):
                global paths
                paths="C:/Users/HP/Desktop/day1/new"
            else:
                paths=input("enter the path:")
            try:
                os.makedirs(paths, exist_ok = True)
            except OSError as error:
                print(error)

    def create(key,value,timeout=0):
        
        if key in d:
            print("error:this key already exist")
        else:
            if(key.isalpha()):
                if len(d)<(1024*1020*1024) and sys.getsizeof(value)<=(16*1024*1024): 
                    if timeout==0:
                        l={"val":value,"timeout":timeout}
                    else:
                        l={"val":value,"timeout":time.time()+timeout}
                    if len(key)<=32:
                        d[key]=l
                        json_object=json.dumps(d,indent=1)
                        with open(paths + "/sample.json","w") as out:
                            out.write(json_object)
                        print("successfully created!!!!!")
                    else:
                        json_object=json.dumps(d,indent=1)
                        with open(paths + "/sample.json","w") as out:
                            out.write(json_object)
                        print("successfully created!!!!!")
                        
                else:
                    print("error: Memory limit exceeded!! ")
            else:
                print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")

                
    def read(key):
        if key not in d:
            print("error: given key does not exist in database. Please enter a valid key") 
        else:
            b=d[key]
            if b["timeout"]!=0:
                if time.time()<b["timeout"]: 
                    with open(paths+"/sample.json","r") as out:
                        json_object=json.load(out)
                        f=json_object[key]
                        print(key + ":"+ str(f["val"]))
                else:
                    print("error: time-to-live of",key,"has expired") 
            else:
                with open(paths+"/sample.json","r") as out:
                    json_object=json.load(out)
                    f=json_object[key]
                    print(key + ":" + str(f["val"]))


    def delete(key):
        if key not in d:
            print("error: given key does not exist in database. Please enter a valid key")
        else:
            b=d[key]
            if b["timeout"]!=0:
                if time.time()<b["timeout"]: 
                    del d[key]
                    print("key is successfully deleted")
                    json_object=json.dumps(d,indent=1)
                    with open(paths + "/sample.json","w") as out:
                        out.write(json_object)
                else:
                    print("error: time-to-live of",key,"has expired")
            else:
                del d[key]
                json_object=json.dumps(d,indent=1)
                with open(paths + "/sample.json","w") as out:
                    out.write(json_object)
                print("key is successfully deleted")
