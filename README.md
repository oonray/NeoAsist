HTB Manager
===========
A program for managing the HTB machines, starting sessions and VPN connections.

Config files are stored in /etc/htb<br/>
VPN file should be stored as /etc/htb/vpn.ovpn<br/>
Default machine storage path is /root/HTB/<br/>

The configuration can be edited.
The programm can be stored at any folder.

Install:
--------
```
cd <your dir>
git clone https://github.com/oonray/HTBManager.git

cd HTBManager
make KEY=<your api key>
make install
```

Overrides:
----------
you can override the following parameters when making.
    *KEY
    *machine_folder

The program will use the path to the directory of the make file to determine the install directory.
The config path must be /etc/HTB as this is hard coded into the application.

example:
```
make KEY=<your api key> machine_folder=<the path where you want the
machines to be stored>

```

USAGE:
------

```
usage: HTBManager2.0.py [-h] [-v] [-s] [-l] [-m M] [-a] action

Manages Hack The Box Machines and Hacking Session

positional arguments:
  action      The action you want to take eg. START, STOP, LIST, DOWNLOAD

optional arguments:
  -h, --help  show this help message and exit

START:
  -v          Target VPN
  -s          Start Session, use with the machine option
  -l          Target last machine
  -m M        Target Machine

LIST:
  -a          Target All

DOWNLOAD:
  -a          Target All

STOP:
  -v          Target VPN
  -s          Start Session, use with the machine option
  -l          Target last machine
  -m M        Target Machine

```
