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
"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
"X-Requested-With":"XMLHttpRequest",
"Authorization":"Bearer {}".format(get_config()["key"]),
"Connection":"close",
"Referer":"https://www.hackthebox.eu/home/machines",
}

"""
+######
| MisC
+######
"""
def write_config(config):
    with open(os.path.join("/etc/HTB/","htb.conf"),"w") as f:
        f.write(json.dumps(config))

def make_url(path):
    return base_url+path

def add_token(url,token):
    ret =  "{}?api_token={}".format(make_url(url),token)
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
argparser.add_argument("-a",help="Target All",action="store_true")
argparser.add_argument("-v",help="Target VPN",action="store_true")
argparser.add_argument("-s",help="Start Session, use with the machine option",action="store_true")
argparser.add_argument("-l",help="Target last machine",action="store_true")
argparser.add_argument("-m",help="Target Machine")

"""
+#######
| Start
+#######
"""
start_group = argparser.add_argument_group("START")

"""
Start Session
"""

def start_tmux(path):
    os.chdir(path)
    os.system("tmux")

def start_session(machine):
    conf = get_config()
    mpath = conf["machines"]
    path = os.popen("find {} -name {}".format(mpath,machine)).read().rstrip()
    start_vpn()
    conf["last"] = machine
    write_config(conf)

    with open(os.path.join(path,"id"),"r") as f:
        ids = int(f.read())

    start_machine(ids)
    start_tmux(path)

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
def start_last():
    conf = get_config()
    start_session(conf["last"])

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
    request =requests.post(make_url(url),headers=post_headders)
    print(request)
    return request

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
    cmd = "mkdir -P {}".format(path)
    cmd2 = "echo '{}' > {}".format(machine["ip"],os.path.join(path,"ip"))
    cmd3 = "echo {} > {}".format(machine["id"],os.path.join(path,"id"))
    os.popen(cmd)
    os.popen(cmd2)
    os.popen(cmd3)
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
"""
def stop_session(machine):
    conf = get_config()
    mpath = conf["machines"]
    path = os.popen("find {} -name {}".format(mpath,machine)).read().rstrip()
    stop_vpn()

    with open(os.path.join(path,"id"),"r") as f:
        ids = int(f.read())

    stop_machine(ids)


"""
Stop Deamon
"""

"""
Stop Machine
"""
def stop_machine(id):
    url = "/api/vm/vip/remove/{}".format(id)
    return requests.post(make_url(url),headers=post_headders)

"""
Stop Last
"""
def stop_last():
    conf = get_config()
    stop_session(conf["last"])

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
         if args.s and args.m:
             start_session(args.m)
         if args.m and not args.s:
             start_machine(args.m)
         if args.l:
             start_last()

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
         if args.s and args.m:
              stop_session(args.m)
         if args.m and not args.s:
              stop_machine(args.m)
         if args.l:
             stop_last()

     if args.action.lower() == "add":
         pass
     if args.action.lower() == "remove":
         pass
     if args.action.lower() == "update":
         pass

