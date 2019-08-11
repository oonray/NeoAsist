requirements = $(PWD)/requirements.txt
config_folder = /etc/HTB
machine_folder = $(HOME)/HTB
KEY = <your api key here>

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

	@echo 
	@echo [.] Creating Config File
	@echo "{" > $(config_folder)/htb.conf
	@echo '"key":"$(KEY)",' >> $(config_folder)/htb.conf
	@echo '"machines":"$(machine_folder)",' >> $(config_folder)/htb.conf
	@echo '"vpnid":0",' >> $(config_folder)/htb.conf
	@echo '"last":""' >> $(config_folder)/htb.conf
	@echo '}' >> $(config_folder)/htb.conf
	
	@echo [+] Generating python Variables
	@echo 'CONF_FOLDER="$(CONF_FOLDER)"' > variables.py
	@echo 'MACHINE_FOLDER="$(machine_folder)"' >> variables.py

install:
	@echo [+] Installing manager from $(PWD)
	'ln -s $(PWD)/HTBmanager.py /usr/bin/HTBmanager'

clean:
	rm /usr/bin/HTBmanager
	cd ~
	rm -rf /etc/htb
	rm -rf /opt/HTBmanager
