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

usage: HTBmanager [start, stop, download, list, add, remove] <target>
