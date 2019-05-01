import requests, os, pickle
from datetime import datetime

BASE_URL = 'https://www.hackthebox.eu/api'
MACHINE_PATH = "/root/HTB/"

def tokenize(path,key):
        return "{}?api_token={}".format(path, key)

class machine:
    def __init__(self,id,name,os,ip,points,release,retired,data):
        self.id = id
        self.name = name
        self.ip = ip
        self.os = os
        self.points = points
        self.release = datetime.strptime(release,"%Y-%m-%d %H:%M:%S")
        self.retired = datetime.strptime(retired,"%Y-%m-%d %H:%M:%S") if retired != None else None
        self.is_Active = True if self.retired == None else False
        self.data=data

    def own_user(self,h,d,key):
        return requests.post(BASE_URL + tokenize('/machines/own/user/{}/'.format(self.id), key), data={"hash": h, "diff": d})

    def own_root(self,h,d,key):
        return requests.post(BASE_URL + tokenize('/machines/own/root/{}/'.format(self.id), key), data={"hash": h, "diff": d})
    
    def reset(slef,key):
        return requests.post(BASE_URL + tokenize('/vm/reset/{}/'.format(id),key))
    
    def create_folder(self,path):
        if(self.is_Active):
            self.location = os.path.join(os.path.join(path,"Active"),self.name)
        else:
            self.location = os.path.join(os.path.join(path,"Retired"),self.name)
        if(not os.path.exists(self.location)):
            os.mkdir(self.location)
        if(not os.path.isfile(os.path.join(self.location,"ip"))):
            with open(os.path.join(self.location,"ip"),"w") as f:
                f.write(self.ip)
        if(not os.path.exists(os.path.join(self.location,"Scan"))):
            os.mkdir(os.path.join(self.location,"Scan"))
    
    def nmap_scan(self):
        self.create_folder(os.path.join(MACHINE_PATH,self.mame))
        os.chdir(self.location)
        os.system("stdscan")

    def save(self): 
        self.create_folder(os.path.join(MACHINE_PATH,self.mame))
        with open(os.path.join(self.location,"machine.json"),"w") as f:
            f.write(json.dumps(self.data))
    
    def load(self):
        self.create_folder(os.path.join(MACHINE_PATH,self.mame))
        with open(os.path.join(self.location,"machine.json"),"r") as f:
            self.data = json.loads(f.read())
        id,name,os,ip,points,release,retired = self.data.values()
        self.__init__(self,id,name,os,ip,points,release,retired)

    def __str__(self):
        return "ID:{s.id:03d} | Name:{s.name:15}| Points:{s.points} | Active:{s.is_Active}".format(s=self)

class get:
    def __init__(self,key):
        self.key = key

    def make_all_machines(self):
        machines = {}
        ret = self.get_machines()
        for i in ret:
            id,name,os,ip,points,release,retired,maker,maker2 = i.values()
            machines[name] = machine(id,name,os,ip,points,release,retired,i)
        return machines

    def get_machines(self):
        return requests.get(BASE_URL + tokenize('/machines/get/all/',self.key)).json()

     

if __name__ == "__main__":
    print(make_all_machines())