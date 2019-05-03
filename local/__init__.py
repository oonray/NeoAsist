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
    os.system("nmap -sV -sC -p- -O -A -oA Scans/TCP `cat ip`")

def UDPScan():
    """LAunches a Nmap UDP Scan

    ..warning:: This should only be used with a sesson open.
    """
    os.system("nmap -sU Scans/UDP `cat ip`")

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

    
    def make_machine(self,name,active):
        return machine(None,name,None,None,None,None,active,None).load()

    def get_machines(self):
        self.get_active()
        self.get_retired()

        for i in self.Active:
             self.machines[i] = self.make_machine(i,None)
        for i in self.Retired:
             self.machines[i] = self.make_machine(i,True)
             
    def get_active(self):
        self.Active = os.listdir(os.path.join(MACHINE_PATH,"Active"))
        for i in self.Active:
            self.machine_path[i]=os.path.join(os.path.join(MACHINE_PATH,"Active"),i)
    
    def get_retired(self):
        self.Retired = os.listdir(os.path.join(MACHINE_PATH,"Retired"))
        for i in self.Retired:
            self.machine_path[i]=os.path.join(os.path.join(MACHINE_PATH,"Retired"),i)

    def list_active(self):
        self.get_machines()
        for i in self.Active:
            print(self.machines[i])
    
    def list_retired(self):
        self.get_machines()
        for i in self.Retired:
            print(self.machines[i])
        
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

    def prtm(self,args2):
        for i in machines.values():
            if i.name == args2.list_machine:
                print(i)
    
    def start_session(self,name):
        status=""
        Active = os.listdir(os.path.join(MACHINE_PATH,"Active"))
        Retired = os.listdir(os.path.join(MACHINE_PATH,"Retired"))
        for i,x in zip(Active,Retired):
            if(i == name):
                status="Active"
            if(x == name):
                status="Retired"

        os.chdir(os.path.join(os.path.join(MACHINE_PATH,status),name))
        try:
            os.system("tmux")
            if(not sum([int(i) for i in getter.conf["vpnid"].split("\n")])>0):
                os.popen("openvpn {}".format(os.path.join(CONFIG_PATH,"vpn.ovpn")))
            ps = os.popen("ps -aux | grep openvpn {}/vpn.ovpn | awk '{print $2}'".format(CONFIG_PATH))
            getter.conf["vpnid"] = ps.read()
            getter.conf["last"] = name
            getter.write(CONFIG_PATH+CONFIG_FILE)  
        except Exception as e:
            print(e)
            exit()

  



