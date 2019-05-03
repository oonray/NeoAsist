"""
:author: Alexander Bjørnsrud <alexanderbjornsrud@gmail.com>
:file: online/__init__.py
:date: 01.05.2019

The functions and variables used in the Online context.
"""

import requests, os, pickle, json
from datetime import datetime

BASE_URL = 'https://www.hackthebox.eu/api'
MACHINE_PATH = "/root/HTB/"

if(not os.path.exists(MACHINE_PATH)):
    os.mkdir(MACHINE_PATH)

if(not os.path.exists(os.path.join(MACHINE_PATH,"Active"))):
        os.mkdir(os.path.join(MACHINE_PATH,"Active"))

if(not os.path.exists(os.path.join(MACHINE_PATH,"Retired"))):
        os.mkdir(os.path.join(MACHINE_PATH,"Retired"))


def tokenize(path,key):
        """Adds an api token to requests
        
        :param path: The API path to request
        :type path: str
        :param key: The api Key
        :type key: str
        :returns: Path with token
        :rtype: str
        """
        return "{}?api_token={}".format(path, key)

class machine:
    def __init__(self,id,name,os,ip,points,release,retired,data):
        """A wrapper around the machine response
        
        :param id: The machine id
        :type id: str
        :param name: The machine name
        :type name: str
        :param os: The operating system of the machine
        :type os: str
        :param ip: The machine ip address
        :type ip: str
        :param points: How many points the machine is worth.
        :type points: str
        :param release: When the machine was released
        :type release: str
        :param retired: When the machine was retured
        :type retired: str
        :param data: The full json String
        :type data: str
        """
        self.id = id
        self.name = name
        self.ip = ip
        self.os = os
        self.points = points
        self.release = datetime.strptime(release,"%Y-%m-%d %H:%M:%S")
        self.retired = datetime.strptime(retired,"%Y-%m-%d %H:%M:%S") if retired != None else None
        self.is_Active = True if self.retired == None else False
        self.data=data
        self.hostname=self.name+".htb"

    def own_user(self,h,d,key):
        """Owns the user on a machine
        
        :param h: The user hash
        :type h: str
        :param d: The difficylty of the box
        :type d: str
        :param key: The API Key
        :type key: str
        :returns: request.response
        :rtype: requests.response
        """
        return requests.post(BASE_URL + tokenize('/machines/own/user/{}/'.format(self.id), key), data={"hash": h, "diff": d})

    def own_root(self,h,d,key):
        """Owns the root user of a machine
        
        :param h: The user hash
        :type h: str
        :param d: The difficylty of the box
        :type d: str
        :param key: The API Key
        :type key: str
        :returns: request.response
        :rtype: requests.response
        """
        return requests.post(BASE_URL + tokenize('/machines/own/root/{}/'.format(self.id), key), data={"hash": h, "diff": d})
    
    def reset(self,key):
        """Resets a machine
        
        :param key: The API key
        :type key: str
        """
        return requests.post(BASE_URL + tokenize('/vm/reset/{}/'.format(id),key))
    
    def create_folder(self):
        """Creates the folder for this machine in the MACHINE_PATH folder

        """
        if(self.is_Active):
            self.location = os.path.join(os.path.join(MACHINE_PATH,"Active"),self.name)
        else:
            self.location = os.path.join(os.path.join(MACHINE_PATH,"Retired"),self.name)
        if(not os.path.exists(self.location)):
            os.mkdir(self.location)
        if(not os.path.isfile(os.path.join(self.location,"ip"))):
            with open(os.path.join(self.location,"ip"),"w") as f:
                f.write(self.ip)
        if(not os.path.exists(os.path.join(self.location,"Scans"))):
            os.mkdir(os.path.join(self.location,"Scans"))

    def save(self): 
        """Saves the machine data in a file in the machine folder
        """
        self.create_folder(os.path.join(MACHINE_PATH,self.name))
        with open(os.path.join(self.location,"machine.json"),"w") as f:
            f.write(json.dumps(self.data))
    
    def load(self):
        """Loads the machine data from file
        """
        self.create_folder(os.path.join(MACHINE_PATH,self.mame))
        with open(os.path.join(self.location,"machine.json"),"r") as f:
            self.data = json.loads(f.read())
        id,name,os,ip,points,release,retired = self.data.values()
        self.__init__(self,id,name,os,ip,points,release,retired)

    def __str__(self):
        return "ID:{s.id:03d} | Name:{s.name:15}| Points:{s.points} | Active:{s.is_Active}".format(s=self)

class onlineget:
    def __init__(self,path):
        self.path=path
        self.load()
        self.key = self.conf["key"]
        self.last = self.conf["last"]
        self.machines = {}

    def make_all_machines(self):
        ret = self.get_machines()
        for i in ret:
            id,name,os,ip,points,release,retired,maker,maker2 = i.values()
            self.machines[name] = machine(id,name,os,ip,points,release,retired,i)
        return self.machines

    def add_to_hosts(self,name="",ip=""):
        with open("/etc/hosts","r") as f:
            hosts = f.readlines()
        machines = {"localhost"}
        for i in hosts:
            if(i[0]!="#" or i[0]!=":" or i[0]!=" "):
                try:
                    computer = i.split()[1]
                    machines.add(computer)
                except Exception as e:
                    print(e)

        if(name != "" and ip != ""):
            for i in hosts:
                if(name.lower() not in i):
                    if(i.split(" ")[0] == ip):
                        line = i[:-1] 
                        line+="{:20}\n".format(name.lower())
                        hosts.remove(i)
                        hosts.append(line)

        else:
            for i in self.machines.values():
                if(i.name.lower() not in machines):
                    hosts.append("{:20}{:20}{:20}\n".format(i.ip,i.name.lower(),i.hostname.lower()))
        with open("/etc/hosts","w") as f:
            f.writelines(hosts)


    def get_machines(self):
        return requests.get(BASE_URL + tokenize('/machines/get/all/',self.key)).json()

    def list_active(self):
        self.make_all_machines()
        active = [i for i in self.machines.values() if i.is_Active]
        return active
    
    def list_retired(self):
        self.make_all_machines()
        retired = [i for i in self.machines.values() if not i.is_Active]
        return retired

    def create(self):
        self.make_all_machines()
        self.add_to_hosts()
        for i in self.machines.values():
            i.create_folder()
            i.save()

    def prt(self,args2):
        if(not args2.active and not args2.retired):
            print("{}[+]{} Printing Machines Avalible".format(Fore.GREEN,Fore.RESET))  
            prt = self.machines.values()
        if(args2.active):
            print("{}[+]{} Printing Active Machines Avalible".format(Fore.GREEN,Fore.RESET))  
            prt = self.list_active()
        if(args2.retired):
            print("{}[+]{} Printing Retired Machines Avalible".format(Fore.GREEN,Fore.RESET))  
            prt = self.list_retired()
        [print(i) for i in prt]

    def prtm(args2):
        for i in machines.values():
            if i.name == args2.list_machine:
                print(i)
    
    def write(self):
        with open(self.path,"w") as f:
            f.write(json.dumps(self.conf))
    
    def load(self):
        with open(self.path,"r") as f:
            self.conf = json.loads(f.read())
