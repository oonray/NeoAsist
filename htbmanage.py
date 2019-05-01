#!/bin//python3
"""
:author: Alexander Bjørnsrud <alexanderbjornsrud@gmail.com>
:file: htbmanage.py
:date: 01.05.2019

This progam is made to manage the different aspects of Hack The Box Automatically.
It is designed to make a structured setup for your machines.
"""

import os, re, sys, argparse, pip, json
from pip._internal import main as pipmain

try:
    import colorama
except:
    pipmain(["install", "-r", "requirements.txt"])

CONFIG_PATH = "/etc/htb/"
CONFIG_FILE = "htb.conf"

if(not os.path.exists(CONFIG_PATH)):
    os.mkdir(CONFIG_PATH)
    with open("./"+CONFIG_FILE,"r") as f1:
        with open(CONFIG_PATH+CONFIG_FILE,"w") as f2:
            f2.write(f1.read())

argparser = argparse.ArgumentParser(description='Manages htb hashes and Machines.')
argparser.add_argument("--online",action="store_true",help="Connect to the htb website, pwn, reset or get boxes")
argparser.add_argument("--local",action="store_true",help="Does local tasks like changes config or runs tools")

"""
Online
"""
parser_online = argparse.ArgumentParser(prog="{} --online".format(sys.argv[0]), description="")
parser_online.add_argument("--get",action="store_true",help="Gets all machines")
parser_online.add_argument("--pwn",action="store_true",help="Submits eighter user or root [require -m and -h]")
#get
parser_online_get = argparse.ArgumentParser(prog="{} --online --get".format(sys.argv[0]), description="")
parser_online_get.add_argument("-p","--print",action="store_true",help="Prints machines to std")
parser_online_get.add_argument("-c","--create",action="store_true",help="Creates machine folders")
parser_online_get.add_argument("-a","--active",action="store_true",help="List only active machines")
parser_online_get.add_argument("-r","--retired",action="store_true",help="List only REtired machines")
#pwn
parser_online_pwn = argparse.ArgumentParser(prog="{} --online --pwn".format(sys.argv[0]), description="")
parser_online_pwn.add_argument("-la","--list-all",action="store_true",help="List online machines")
parser_online_pwn.add_argument("-lm","--list-machine",type=str,help="List a single machine by name")
parser_online_pwn.add_argument("-a","--active",action="store_true",help="List only active machines")
parser_online_pwn.add_argument("-r","--retired",action="store_true",help="List only REtired machines")
parser_online_pwn.add_argument("-m","--machine",type=int,help="The machine id to pwn")
parser_online_pwn.add_argument("--user",action="store_true",help="Own user")
parser_online_pwn.add_argument("--root",action="store_true",help="Own root")
parser_online_pwn.add_argument("-hs","--hash",type=str,help="The machine to pwn")
parser_online_pwn.add_argument("-s","--score",type=int,help="The machine to pwn")


"""
Local
"""
parser_local = argparse.ArgumentParser(prog="{} --local".format(sys.argv[0]),description="")
parser_local.add_argument("-l","--list",help="Lists all local machines")
parser_local.add_argument("-a","--active",action="store_true",help="List only active machines")
parser_local.add_argument("-r","--retired",action="store_true",help="List only REtired machines")
parser_local.add_argument("-k","--key",type=str,help="Change API Key")
parser_local.add_argument("--install",help="Install dependencies")
parser_local.add_argument("-ss","--start-session",type=str,help="Starts Tmux session with the local machine name provided")
parser_local.add_argument("--scan",type=str,help="starts the auto scan")
parser_local.add_argument("-ah","--add-host",type=str,help="adds host to the ip")
parser_local.add_argument("-ip","--ip",type=str,help="ip of the machine to change")


if(sys.argv[1:2]==[]):
        argparser.print_usage()
        exit()

base_arg = argparser.parse_args(sys.argv[1:2])        

if(base_arg.online):
    from online import get, MACHINE_PATH

    try:
        with open(os.path.join(CONFIG_PATH,CONFIG_FILE),"r") as f:
                conf = json.loads(f.read())
                getter = get(conf["key"])
    except:
            out = "You Must Add an api key to {}{}".format(CONFIG_PATH,CONFIG_FILE)
            raise ValueError(out)
    
    parser = parser_online
    if(sys.argv[2:3]==[]):
            parser.print_usage()
            exit()

    args = parser.parse_args(sys.argv[2:3])

    if(args.get):
        parser2 = parser_online_get
    if(args.pwn):
        parser2 = parser_online_pwn

    if(sys.argv[3:4]==[]):
            parser2.print_usage()
            exit()

    args2 = parser2.parse_args(sys.argv[3:])

    parsed = (base_arg,args,args2)

  
        
    machines = getter.make_all_machines()
    if(args.get):
        if(args2.create):
            getter.add_to_hosts()
            for i in machines.values():
                i.create_folder(MACHINE_PATH)
            
        if(args2.print):
            if(not args2.active and not args2.retired):
                    prt = machines.values()
            if(args2.active):
                    prt = getter.list_active()
            if(args2.retired):
                    prt = getter.list_retired()
            [print(i) for i in prt]
                

    if(args.pwn):
        if(args2.list_all):
            if(not args2.active and not args2.retired):
                    prt = machines.values()
            if(args2.active):
                    prt = getter.list_active()
            if(args2.retired):
                    prt = getter.list_retired()
            [print(i) for i in prt]
                

        if(args2.list_machine):
            for i in machines.values():
                if i.name == args2.list_machine:
                    print(i)
        
        if(args2.machine):
            if(not args2.hash and args2.score):
                    parser2.print_help()
                    exit()

            if(not args2.root or args2.user):
                    parser2.print_help()
                    exit()

            if(args2.root and args2.user):
                parser2.print_help()
                exit()

            if(args2.user):
                getter.machines[args2.machines].own_user(args2.hash,args2.score,key)
            if(args2.root):
                getter.machines[args2.machines].own_root(args2.hash,args2.score,key)
        
if(base_arg.local):
    from online import get,MACHINE_PATH

    parser = parser_local
    if(sys.argv[2:3]==[]):
            parser.print_usage()
            exit()
    args = parser.parse_args(sys.argv[2:])    
    if(args.list):
        Active = os.listdir(os.path.join(MACHINE_PATH,"Active"))
        Retired = os.listdir(os.path.join(MACHINE_PATH,"Retired"))
        if(not args.active or not args.retired):
            args.active,args.retired = True,True
        if(args.active):
            [print(i) for i in Active]
        if(args.retired):
            [print(i) for i in Retired]
    
    if(args.key):
        with open(CONFIG_PATH+CONFIG_FILE,"r") as f:
           data = json.laods(f.read())
           data["key"] = args.key 
        with open(CONFIG_PATH+CONFIG_FILE,"w") as f:
           f.write(json.dumps(data))

    if(args.install):
        os.system("sudo apt-get install tmux -y")

    if(args.start_session):
        status=""
        Active = os.listdir(os.path.join(MACHINE_PATH,"Active"))
        Retired = os.listdir(os.path.join(MACHINE_PATH,"Retired"))
        for i,x in zip(Active,Retired):
            if(i == args.start_session):
                status="Active"
            if(x == args.start_session):
                status="Retired"
        try:
            os.chdir(os.path.join(os.path.join(MACHINE_PATH,status),args.start_session))
            os.popen("openvpn {}".format(os.path.join(CONFIG_PATH,"vpn.ovpn")))
            os.system("tmux")
        except Exception as e:
            print(e)
            raise ValueError("The machine does not exist!")

    if(args.add_host):
        if(not args.ip):
            parser.print_help()
            exit()
        getter = get("")
        getter.add_to_hosts(args.add_host,args.ip)
            
    







