#!/usr/bin/python3
"""
:author: Alexander Bjørnsrud <alexanderbjornsrud@gmail.com>
:file: htbmanage.py
:date: 11.08.2019

This progam is made to manage the different aspects of Hack The Box Automatically.
It is designed to make a structured setup for your machines.
"""
import variables
import argparse

argparser = argparse.ArgumentParser(description="Manages Hack The Box Machines and Hacking Session")


url="https://www.hackthebox.eu/"
machine_url="/machines/get/all"

def add_token(url,token):
    return "{}?api_token={}".format(url,token)

print("{}\n{}".format(variables.MACHINE_FOLDER,variables.CONF_FOLDER))

"""
Start Session
"""
def start_session():
    pass
"""
Start VPN
"""
def start_vpn():
   pass


"""
Start Last
"""
def start_last():
    pass

"""
Start STD Scans
Start Lease
"""



"""
List Machines
List Active
List Retired
List OSCP
"""

"""
Download ALL
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



