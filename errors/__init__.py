from colorama import *

init()

def base_string():

    return "{}[!]{}".format(Fore.RED,Style.RESET_ALL)

def print_error(error):
    print("{}{}".format(base_string(),error))
    exit()

def fetch_error():
    print_error("Could not fetch Data.")

def file_open_error(file):
    print_error("Could not open file {}".format(file))
