#!/usr/bin/python3
"""
:author: Alexander Bjørnsrud <alexanderbjornsrud@gmail.com>
:file: htbmanage.py
:date: 11.08.2019

This progam is made to manage the different aspects of Hack The Box Automatically.
It is designed to make a structured setup for your machines.
"""
import argparse, json, sys, os, requests, colorama

def get_config():
    with open(os.path.join("/etc/HTB/","htb.conf"),"r") as f:
         return json.loads(f.read())

conf = get_config()
sys.path.append(conf["install"])

from errors import *

init()

argparser = argparse.ArgumentParser(description="Manages Hack The Box Machines and Hacking Session")


base_url = "https://www.hackthebox.eu/api"
headers = {"User-Agent":"curl/7.65.1"}
post_headders = {
"Host":"www.hackthebox.eu",
"User-Agent":" Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
"X-Requested-With":" XMLHttpRequest",
"Authorization":" Bearer pVkNxdRdmZYMiPMeCO6KqPvJvRtAanGRn6eieRD8YxPwo6T7AfbPFpmWyczm",
"Connection":" close",
"Referer":" https://www.hackthebox.eu/home/machines",
}

"""
+######
| MisC
+######
"""
def write_config(config):
    with open(os.path.join("/etc/HTB/","htb.conf"),"w") as f:
        f.write(json.dumps(config))

def add_token(url,token):
    ret =  "{}{}?api_token={}".format(base_url,url,token)
    return ret

def get_api_token():
    conf = get_config()
    key = conf["key"]
    if(key=="<your api key here>"):
        print("You must add a api key to {}/htb.conf".format("/etc/HTB"))
        exit()
    return key


def get(url):
    request = requests.get(url,headers=headers)
    check_response(request)
    return request

def check_response(response):
    if response.status_code != 200:
        fetch_error()

argparser.add_argument("action",help="The action you want to take eg. START, STOP, LIST, DOWNLOAD")
argparser.add_argument("-a",help="target all All",action="store_true")
argparser.add_argument("-v",help="target VPN",action="store_true")

"""
+#######
| Start
+#######
"""
start_group = argparser.add_argument_group("START")

"""
Start Session
"""
start_group.add_argument("-s",help="Session, Machine To start session with")

def start_session(machine):
    conf = get_config()
    mpath = conf["machines"]
    path = os.popen("find {} -name {}".format(mpath,machine)).read()
    print(path)


"""
Start VPN
"""
def start_vpn():
   conf = get_config()
   ids = [int(i) for i in conf["vpnid"].split("\n") if i != ""]

   if sum(ids) > 0:
      return 1

   path = os.path.join("/etc/HTB/","vpn.ovpn")
   if os.path.exists(path) == False:
       file_open_error(path)
   os.popen("openvpn {}".format(os.path.join("/etc/HTB/","vpn.ovpn"))
           )

   ps = os.popen('ps -aux | grep {} | awk \'{}print $2{}\''.format(path,"{","}")).read()
   conf["vpnid"] = ps
   write_config(conf)
   return 0

"""
Start Last session
"""
start_group.add_argument("-l",help="Continue the last session", action="store_true")
def start_last():
    pass

"""
Start STD Scans
"""
"""
Start Deamon
"""
"""
Start Machine
"""
def start_machine(id):
    url = "/vm/vip/assign/{}".format(id)
    requests.post(url,headders=post_headders)

"""
Start Tmux
"""

"""
+######
| LIST
+######
"""
list_group = argparser.add_argument_group("LIST")

"""
List Machines
"""
def get_all_machines():
   url = "/machines/get/all"
   return get(add_token(url,get_api_token()))

def parse_all_machines(request):
    ret = {}
    parsed_data = json.loads(request.text)
    for i in parsed_data:
         ret[i["name"]] = i
    return ret

def print_all_machines(machines_parsed):
    for i in machines_parsed:
        print(i)

"""
List Active
List Retired
List OSCP
"""

"""
+##########+
| Download
+##########+
"""
download_group = argparser.add_argument_group("DOWNLOAD")

"""
Download ALL
"""

def make_directory(machine):
    conf = get_config()

    location = "Active" if machine["retired_date"] == None else "Retired"
    if machine["name"] in conf["OSCP"]:
        location = "OSCP"

    path = os.path.join(conf["machines"],
                os.path.join(location,
                     os.path.join(
                         machine["os"], machine["name"]
                    )
                )
          )
    cmd = "mkdir {}".format(path)
    cmd2 = "echo '{}' > {}".format(machine["ip"],os.path.join(path,"ip"))
    os.system(cmd)
    os.system(cmd2)
    return True
"""
+###########
| STOP
+###########
"""
stop_grop = argparser.add_argument_group("STOP")

"""
Stop VPN
"""

def stop_vpn():
    conf = get_config()
    os.system('for i in $(ps -aux | grep {} | awk \'{}print $2{}\'); do kill $i;done'.format(os.path.join("/etc/HTB/","vpn.ovpn"),"{","}"))
    conf["vpnid"]="0\n"
    write_config(conf)


"""
Stop Session
Stop Deamon
"""

"""
Stop Machine
"""
def stop_machine(id):
    url = "/api/vm/vip/remove/{}".format(id)

"""
Add Host to /etc/hosts
"""

"""
Remove Host form /etc/hosts
"""

if __name__ == "__main__":
     args = argparser.parse_args()
     #start list downlad stop add remove update
     if args.action.lower() == "start":
         if args.v:
             start_vpn()
     if args.action.lower() == "list":
         if args.a:
             print_all_machines(parse_all_machines(get_all_machines()))
     if args.action.lower() == "download":
         if args.a:
             m = parse_all_machines(get_all_machines())
             for i in m.values():
                 make_directory(i)

     if args.action.lower() == "stop":
         if args.v:
             stop_vpn()

     if args.action.lower() == "add":
         pass
     if args.action.lower() == "remove":
         pass
     if args.action.lower() == "update":
         pass

     a = parse_all_machines(get_all_machines())
     print(a["Helpline"])
     print(get_config())
     start_session("Bastard")
     start_machine(7)
