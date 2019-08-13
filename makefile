requirements = $(PWD)/requirements.txt
config_folder = /etc/HTB
machine_folder = $(HOME)/HTB
KEY = <your api key here>
active =$(machine_folder)/Active

all:
	@echo [+] Installing Reqirements
	@echo [.]Getting Latest updates.
	sudo apt-get update && sudo apt-get upgrade	
	
	@echo 	
	@echo [.] Installing Python3
	sudo apt-get install python3 python3-pip -y

	@echo 
	@echo [.] Installing pip requirements from $(requirements) 
	pip install -r $(requirements)
	
	@echo
	@echo [+] Creating Config 
	@echo [.] Creating Config Folder $(config_folder)
	sudo rm -rf $(config_folder)
	sudo mkdir $(config_folder)
	sudo chown $(USER) $(config_folder)

	@echo [+] Creating Machine Folders
	mkdir $(machine_folder)
	mkdir $(active)
	mkdir $(active)/Linux
	mkdir $(active)/Windows
	mkdir $(active)/FreeBSD
	mkdir $(active)/Other

	mkdir $(machine_folder)/Retired
	mkdir $(machine_folder)/Retired/Linux
	mkdir $(machine_folder)/Retired/Windows
	mkdir $(machine_folder)/OSCP/FreeBSD
	mkdir $(machine_folder)/OSCP/Other

	mkdir $(machine_folder)/OSCP/
	mkdir $(machine_folder)/OSCP/Linux
	mkdir $(machine_folder)/OSCP/Windows
	mkdir $(machine_folder)/OSCP/FreeBSD
	mkdir $(machine_folder)/OSCP/Other
	

	@echo 	
	@echo [.] Creating Config File
	@echo '{' > $(config_folder)/htb.conf
	@echo '"key":"$(KEY)",' >> $(config_folder)/htb.conf
	@echo '"machines":"$(machine_folder)",' >> $(config_folder)/htb.conf
	@echo '"vpnid":"0",' >> $(config_folder)/htb.conf
	@echo '"last":""' >> $(config_folder)/htb.conf
	@echo '}' >> $(config_folder)/htb.conf
	
	@echo [+] Generating python Variables
	@echo 'CONF_FOLDER="$(config_folder)"' > variables.py
	@echo 'MACHINE_FOLDER="$(machine_folder)"' >> variables.py
	@echo 'OSCP = ["Lame","Branfuck","Shocker","Bashed","Nibbles","Beep","Cronos","Nineveh","Sencse","Solidstate","Kotark","Node","Valentine","Poison","Sunday","Tartarsause","Legacy","Blue","Devel","Optimum","Bastard","Granny","Arctic","Grandpa","Silo","Bounty","Jerry"]' >> variables.py

install:
	@echo [+] Installing manager from $(PWD)
	'ln -s $(PWD)/HTBmanager.py /usr/bin/HTBmanager'

clean:
	rm /usr/bin/HTBmanager
	cd ~
	rm -rf /etc/htb
	rm -rf /opt/HTBmanager
