"""
:author: Alexander Bjørnsrud <alexanderbjornsrud@gmail.com>
:file: local/__init__.py
:date: 01.05.2019


The functions used in the setting.

"""
import os, json

def TCPScan():
    """Launches an Nmap TCP Scan

    ..warning:: This should only be used with a sesson open.
    """
    os.popen("nmap -sV -sC -p- -O -A -oA Scans/TCP `cat ip`")

def UDPScan():
    """LAunches a Nmap UDP Scan

    ..warning:: This should only be used with a sesson open.
    """
    os.popen("nmap -sU Scans/UDP `cat ip`")

def stdscan():
    """Runs both TCP and UDP scans

    ..warning:: This should only be used with a sesson open.
    """
    TCPScan()
    UDPScan()

from online import onlineget, machine, MACHINE_PATH

class localget(onlineget):
    def __init__(self,conf):
        onlineget.__init__(self,conf)
        self.machine_path = {}

    def make_all_machines(self):
        ret = self.get_machines()
        for i in ret:
            id,name,os,ip,points,release,retired,maker,maker2 = i.values()
            self.machines[name] = machine(id,name,os,ip,points,release,retired,i)
        return self.machines

    
    def make_machine(self,name):
        ret = self.get_machine(name)
        id,name,os,ip,points,release,retired,maker,maker2 = ret.values()
        return machine(id,name,os,ip,points,release,retired,i)

    def get_machines(self):
        self.get_active()
        self.get_retired()
        data = []
        for i,x in zip(self.machine_path,self.machine_path.values):
             data.append(json.loads(x+i+".json"))
        return data

    def get_machine(self,name):
        self.get_active()
        self.get_retired()
        return json.loads(self.machine_path[name]+name+".json")

    def get_active(self):
        self.Active = os.listdir(os.path.join(MACHINE_PATH,"Active"))
        for i in self.Active:
            self.machine_path[i]=os.path.join(os.path.join(MACHINE_PATH,"Active"),i)
    
    def get_retired(self):
        self.Retired = os.listdir(os.path.join(MACHINE_PATH,"Retired"))
        for i in self.Retired:
            self.machine_path[i]=os.path.join(os.path.join(MACHINE_PATH,"Retired"),i)

    def list_active(self):
        self.get_active()
        for i in self.Active:
            print(self.make_machine(i))
    
    def list_retired(self):
        self.get_retired()
        for i in self.Retired:
            print(self.make_machine(i))
        
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
    


