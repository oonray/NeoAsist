install:
	sudo apt-get install python3 -y
	sudo apt-get install python3-pip -y
	./HTBmanager.py --install
	ln -s /opt/HTBmanager/HTBmanager.py /usr/bin/HTBmanager

clean:
	rm /usr/bin/HTBmanager
	cd ~
	rm -rf /etc/htb
	rm -rf /opt/HTBmanager
