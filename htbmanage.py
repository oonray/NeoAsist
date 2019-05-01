"""
:author: Alexander Bjørnsrud <alexanderbjornsrud@gmail.com>
:author: Rene Østensen <contact@zorko.co>
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
argparser.add_argument("--all",action="store_true",help="Runs all opperations. Good for a fresh start.")
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
#pwn
parser_online_pwn = argparse.ArgumentParser(prog="{} --online --pwn".format(sys.argv[0]), description="")
parser_online_pwn.add_argument("-m","--machine",action="store_true",help="The machine to pwn")

"""
Local
"""
parser_local = argparse.ArgumentParser(prog="{} --local".format(sys.argv[0]),description="")

if(sys.argv[1:2]==[]):
        argparser.print_usage()
        exit()

base_arg = argparser.parse_args(sys.argv[1:2])        

if(base_arg.all):
        pass
if(base_arg.local):
        parser = parser_local
if(base_arg.online):
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

if(base_arg.online):
    from online import get, MACHINE_PATH
    try:
        with open(os.path.join(CONFIG_PATH,CONFIG_FILE),"r") as f:
            conf = json.loads(f.read())
            getter = get(conf["key"])
    except:
        raise ValueError("You Must Add an api key to {}".format(CONFIG_PATH))
        
    machines = getter.make_all_machines()
    if(args.get):
        if(args2.create):
            for i in machines.values():
                i.create_folder(MACHINE_PATH)
                
        if(args2.print):
            [print(i) for i in machines.values()]
        
        

if(base_arg.local):
    pass






