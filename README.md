HTB Manager
===========
A program for managing the HTB machines, starting sessions and VPN connections.

Config files are stored in /etc/htb<br/>
VPN file should be stored as /etc/htb/vpn.ovpn<br/>
Default machine storage path is /root/HTB/<br/>

The configuration can be edited.

Install:
--------
```
cd /opt/
git clone https://github.com/oonray/HTBManager.git

cd HTBManager
make install
```

usage: HTBmanager [-h] [--online] [--local] [--install]