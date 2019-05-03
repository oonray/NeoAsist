install:
	sudo apt-get install python3 -y
	sudo apt-get install python3-pip -y
	./HTBmanager --install
	ln /opt/HTBManager/HTBmanager.py /usr/bin/HTBmanager

clean:
	rm /usr/bin/HTBManager
	cd ~
	rm -rf /opt/HTBManager
