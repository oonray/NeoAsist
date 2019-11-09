#!/usr/bin/python3
"""
:author: Alexander Bjørnsrud <alexanderbjornsrud@gmail.com>
:file: htbmanage.py
:date: 11.08.2019

This progam is made to manage the different aspects of Hack The Box Automatically.
It is designed to make a structured setup for your machines.
"""
import argparse, json, sys, os, requests, colorama, subprocess

def get_config():
    with open(os.path.join("/etc/HTB/","htb.conf"),"r") as f:
         return json.loads(f.read())

conf = get_config()
sys.path.append(conf["install"])

from errors import *

init()

argparser = argparse.ArgumentParser(description="Manages Hack The Box Machines and Hacking Session")
argparser.add_argument("action",help="The action you want to take eg. START, STOP, LIST, DOWNLOAD")


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

def get_id(machine):
    conf = get_config()
    mpath = conf["machines"]
    path = os.popen("find {} -name {}".format(mpath,machine)).read().rstrip()

    with open(os.path.join(path,"id"),"r") as f:
         return int(f.read())

def get(url):
    request = requests.get(url,headers=headers)
    check_response(request)
    return request

def check_response(response):
    if response.status_code != 200:
        print(response.url)
        fetch_error()

"""
+#######
| Start
+#######
"""
start_group = argparser.add_argument_group("START")
t_vpn = start_group.add_argument("-v",help="Target VPN",action="store_true")
t_session = start_group.add_argument("-s",help="Start Session, use with the machine option",action="store_true")
t_last = start_group.add_argument("-l",help="Target last machine",action="store_true")
t_machine = start_group.add_argument("-m",help="Target Machine")


"""
Start Session
"""

def start_session(machine):
    conf = get_config()
    mpath = conf["machines"]
    path = os.popen("find {} -name {}".format(mpath,machine)).read().rstrip()
    start_vpn()
    conf["last"] = machine
    write_config(conf)

    start_machine(get_id(machine))
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
Start Deamon
"""
"""
Start Machine
"""
def start_machine(id):
    url = "/vm/vip/assign/{}".format(id)
    request =requests.post(make_url(url),headers=post_headders)
    print(id,request.text)
    return request

"""
Start Tmux
"""
def start_tmux(path):
    os.chdir(path)
    os.system("tmux")

"""
+######
| LIST
+######
"""
list_group = argparser.add_argument_group("LIST")
t_all = list_group.add_argument("-a",help="Target All",action="store_true")
t_owns = list_group.add_argument("-o",help="Target Owns",action="store_true")
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

def id_all_machines(request):
    ret = {}
    parsed_data = json.loads(request.text)
    for i in parsed_data:
        ret[i["id"]] = i
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
download_group._group_actions.append(t_all)
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
    cmd = "mkdir -p {}".format(path)
    cmd2 = "echo '{}' > {}".format(machine["ip"],os.path.join(path,"ip"))
    cmd3 = "echo {} > {}".format(machine["id"],os.path.join(path,"id"))

    try:
        subprocess.check_output(cmd.split())
        os.popen(cmd2)
        os.popen(cmd3)
    except:
        subprocess.check_output(cmd.split())
        os.popen(cmd2)
        os.popen(cmd3)

    return True
"""
+###########
| STOP
+###########
"""
stop_grop = argparser.add_argument_group("STOP")
stop_grop._group_actions.append(t_vpn)
stop_grop._group_actions.append(t_session)
stop_grop._group_actions.append(t_last)
stop_grop._group_actions.append(t_machine)


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
    stop_machine(get_id(machine))


"""
Stop Deamon
"""

"""
Stop Machine
"""
def stop_machine(id):
    url = "/vm/vip/remove/{}".format(id)
    request =requests.post(make_url(url),headers=post_headders)
    print(id,request.text)
    return request
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

"""
+####
|UPDATE
+#####
"""
update_group = argparser.add_argument_group("UPDATE")

def get_owns():
    url = "/machines/owns"
    request = get(add_token(url,get_api_token()))
    return request

def update_owns(owns):
    conf = get_config()
    cmd = "find {} -name {} -type d"

    owns = json.loads(get_owns().text)
    machines = id_all_machines(get_all_machines())
    modify = []

    for i in owns:
        ids,owned_user,owned_root = i.values()
        if owned_root:
            modify.append(machines[ids]["name"])

    print(modify)

    for i in modify:
        path = os.popen(cmd.format(conf["machines"],i)).read().strip()
        print(path)
        if "DONE" not in path and " " not in path and path != "":
            try:
               status, m_os, name = path.split("/")[-3:]
            except:
                print("PATH:"+path)
                print(path.split("/"))
                status, m_os, name = path.split("/")[-3:]

            new_path = os.path.join(
                       os.path.join(
                         os.path.join(conf["machines"],"DONE"),
                           status),
                         m_os)
            cmd = "mkdir -p {}".format(new_path)
            try:
                subprocess.check_call(cmd.split())
            except:
                subprocess.check_call(cmd.split())
            cmd2 = "mv {} {}".format(path,new_path)
            try:
               subprocess.check_call(cmd2.split())
            except:
               subprocess.check_call(cmd2.split())

if __name__ == "__main__":
     args = argparser.parse_args()
     #start list downlad stop add remove update
     if args.action.lower() == "start":
         if args.v:
             start_vpn()
         if args.s and args.m:
             start_session(args.m)
         if args.m and not args.s:
             start_machine(get_id(args.m))
         if args.l:
             start_last()

     if args.action.lower() == "list":
         if args.a:
             print_all_machines(parse_all_machines(get_all_machines()))
         if args.o:
             print_all_machines(parse_all_machines(get_owns()))

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
              stop_machine(get_id(args.m))
         if args.l:
             stop_last()

     if args.action.lower() == "add":
         pass
     if args.action.lower() == "remove":
         pass
     if args.action.lower() == "update":
         update_owns(get_owns())

     update_owns(get_owns())

