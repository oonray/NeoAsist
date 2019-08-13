import colorama

colorama.init()

def base_string():
    return "{}[!]{}".format(colorama.Fore.RED,colorama.Fore.RESET_ALL)

def print_error(error):
    print("{}{}".format(base_strint(),error))
    exit()

def fetch_error():
    print_error("Could not fetch Data.")

