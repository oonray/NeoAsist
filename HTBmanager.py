#!/bin//python3
"""
:author: Alexander Bjørnsrud <alexanderbjornsrud@gmail.com>
:file: htbmanage.py
:date: 01.05.2019

This progam is made to manage the different aspects of Hack The Box Automatically.
It is designed to make a structured setup for your machines.
"""

import os, re, sys, argparse, pip, json
from subprocess import Popen, PIPE
from pip._internal import main as pipmain

CONFIG_PATH = "/etc/htb/"
CONFIG_FILE = "htb.conf"

argparser = argparse.ArgumentParser(description='Manages htb hashes and Machines.')
argparser.add_argument("--online",action="store_true",help="Connect to the htb website, pwn, reset or get boxes")
argparser.add_argument("--local",action="store_true",help="Does local tasks like changes config or runs tools")
argparser.add_argument("--install",action="store_true",help="Install dependencies")

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

parser_online_pwn.add_argument("-m","--machine",type=int,help="The machine name to pwn")
parser_online_pwn.add_argument("--user",action="store_true",help="Own user")
parser_online_pwn.add_argument("--root",action="store_true",help="Own root")
parser_online_pwn.add_argument("-hs","--hash",type=str,help="The machine to pwn")
parser_online_pwn.add_argument("-s","--score",type=int,help="The machine to pwn")


"""
Local
"""
parser_local = argparse.ArgumentParser(prog="{} --local".format(sys.argv[0]),description="")
parser_local.add_argument("-l","--list",action="store_true",help="Lists all local machines")
parser_local.add_argument("-a","--active",action="store_true",help="List only active machines")
parser_local.add_argument("-r","--retired",action="store_true",help="List only REtired machines")

parser_local.add_argument("-k","--key",type=str,help="Change API Key")

parser_local.add_argument("-ah","--add-host",type=str,help="adds host to the ip")
parser_local.add_argument("-ip","--ip",type=str,help="ip of the machine to change")
parser_local.add_argument("-kv","--kill_vpn",action="store_true",help="ip of the machine to change")

parser_local.add_argument("-stds","--std_scan",action="store_true",help="Start tcp and udp scan")
parser_local.add_argument("-ss","--start-session",type=str,help="Starts Tmux session with the local machine name provided")
parser_local.add_argument("-sl","--start_last",action="store_true",help="used with -ss starts last used sesson")


if(sys.argv[1:2]==[]):
        argparser.print_usage()
        exit()

base_arg = argparser.parse_args(sys.argv[1:2])

if(base_arg.install):
    print("[+] Installing Requirements")
    print("[+] Installing Pip requirements")
    pipmain(["install", "-r", "requirements.txt"])
    print("[+] Installing tmux")
    os.system("sudo apt-get install tmux -y")
    print("[+] Installing openvpn")
    os.system("sudo apt-get install openvpn -y")
    
    print("[+] Creating Config Folder: {}".format(CONFIG_PATH))
    if(not os.path.exists(CONFIG_PATH)):
        os.mkdir(CONFIG_PATH)
    
    print("[+] Creating Config File {}".format(CONFIG_FILE))
    with open("./"+CONFIG_FILE,"r") as f1:
            with open(CONFIG_PATH+CONFIG_FILE,"w") as f2:
                f2.write(f1.read())


from colorama import init, Fore
init(autoreset=True)       

if(base_arg.online):
    from online import onlineget, MACHINE_PATH

    try:
        print("{}[+]{} Loading Config".format(Fore.GREEN,Fore.RESET))
        getter = onlineget(CONFIG_PATH+CONFIG_FILE)
        getter.load()
    except:
            out = "{}[!]{} You Must Add an api key to {}{}".format(Fore.RED,Fore.RESET,CONFIG_PATH,CONFIG_FILE)
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
            print("{}[+]{} Creating Machines in {}".format(Fore.GREEN,Fore.RESET,MACHINE_PATH))
            getter.create()
            
        if(args2.print):          
            getter.prt()
                

    if(args.pwn):
        if(args2.list_all):
            getter.prt(args2)
                
        if(args2.list_machine):
            getter.prt(args2)
        
        if(not args2.machine):
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
    from online import MACHINE_PATH
    from local import *

    getter = localget(CONFIG_PATH+CONFIG_FILE)
    getter.load()

    parser = parser_local
    if(sys.argv[2:3]==[]):
            parser.print_usage()
            exit()
    args = parser.parse_args(sys.argv[2:])    
    if(args.list):
        if(not args.active and not args.retired):
            args.active,args.retired = True,True
            getter.list_active()
            getter.list_retired()
        if(args.active):
            getter.list_active()
        if(args.retired):
            getter.list_retired()
    
    if(args.key):
        getter.conf["key"] = args.key 
        with open(CONFIG_PATH+CONFIG_FILE,"w") as f:
           f.write(json.dumps(getter.conf))

    if(args.start_session):
            getter.start_session(args.start_session,os.path.join(CONFIG_PATH,"vpn.ovpn"))

    if(args.start_last):
            getter.start_session(getter.last,os.path.join(CONFIG_PATH,"vpn.ovpn"))
    
    if(args.kill_vpn):
        os.system('for i in $(ps -aux | grep '+"{}vpn.ovpn | awk ".format(CONFIG_PATH)+'\'{print $2}\'); do kill $i; done')
        getter.conf["vpnid"]="0"
        getter.write()

    if(args.add_host):
        if(not args.ip):
            parser.print_help()
            exit()
        getter.add_to_hosts(args.add_host,args.ip)
    
    if(args.std_scan):
        stdscan()

    