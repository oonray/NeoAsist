install:
	sudo apt-get install python3
	sudo apt-get instapp python3 pip
	./HTBmanager --install
	ln /opt/HTBManager/HTBmanager.py /usr/bin/HTBmanager

clean:
	rm /usr/bin/HTBManager
	cd ~
	rm /opt/HTBManager
