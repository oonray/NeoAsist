#!/usr/bin/python3
"""
:author: Alexander Bjørnsrud <alexanderbjornsrud@gmail.com>
:file: htbmanage.py
:date: 11.08.2019

This progam is made to manage the different aspects of Hack The Box Automatically.
It is designed to make a structured setup for your machines.
"""
import variables, argparse, json. sys, os

argparser = argparse.ArgumentParser(description="Manages Hack The Box Machines and Hacking Session")


base_url="https://www.hackthebox.eu/"

"""
+######
| MisC
+######
"""
def add_token(url,token):
    return "{}/{}?api_token={}".format(base_url,url,token)

def get_api_token():
    with open(os.path.join(variables.CONF_FOLDER,"htb.conf")) as f:
        key = json.loads(f.read())["key"]
        if(key=="<your api key here>"):
            print("You must add a api key to {}/htb.conf".format(variables.CONF_FOLDER))
            exit()
        return key

argparser.add_argument("action",help="The action you want to take eg. START, LIST, DOWNLOAD")

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
def start_session():
    pass

"""
Start VPN
"""
start_group.add_argument("-v",help="Start VPN conneciton",action="store_true")
def start_vpn():
   pass


"""
Start Last
"""
start_group.add_argument("-l",help="Continue the last session", action="store_true")
def start_last():
    pass

"""
Start STD Scans
Start Lease
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
list_group.add_argument("-m",help="Lists active machines")
def list_all_machines():
   url = "/machines/get/all"
   add_token(url,get_api_token())
   pass

def print_all_machines(machines):
    print(machines)

"""
List Active
List Retired
List OSCP
"""

"""
Download ALL
"""
def download_all():
    pass


"""
Download Active
Download Retired
Download OSCP
"""

"""
Stop VPN
Stop Lease
"""

"""
Add Host to /etc/hosts
"""

"""
Remove Host form /etc/hosts
"""



