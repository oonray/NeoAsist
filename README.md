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
    *config_folder
    *machine_folder

example:
```
make KEY=<your api key> config_folder=<your config path> machine_folder=<the path where you want the
machines to be stored>

```
usage: HTBmanager [-h] [--online] [--local] [--install]
