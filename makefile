requirements = $(PWD)/requirements.txt
config_folder = /etc/HTB
machine_folder = $(HOME)/HTB
challenge_folder = $(machine_folder)/Challenges
fortress_folder = $(machine_folder)/Fortress
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
	mkdir -p $(active)/Linux
	mkdir -p $(active)/Windows
	mkdir -p $(active)/FreeBSD
	mkdir -p $(active)/Other
	mkdir -p $(active)/Solaris

	mkdir -p $(machine_folder)/Retired/Linux
	mkdir -p $(machine_folder)/Retired/Windows
	mkdir -p $(machine_folder)/Retired/FreeBSD
	mkdir -p $(machine_folder)/Retired/Other
	mkdir -p $(machine_folder)/Retired/Solaris
	
	mkdir -p $(machine_folder)/OSCP/Linux
	mkdir -p $(machine_folder)/OSCP/Windows
	mkdir -p $(machine_folder)/OSCP/FreeBSD
	mkdir -p $(machine_folder)/OSCP/Other
	mkdir -p $(machine_folder)/OSCP/Solaris	
    
	mkdir -p $(machine_folder)/DONE

	mkdir -p $(challenge_folder)
	mkdir -p $(fortress_folder)

	@echo 	
	@echo [.] Creating Config File
	@echo '{' > $(config_folder)/htb.conf
	
	@echo [.] Adding the key
	@echo '"key":"$(KEY)",' >> $(config_folder)/htb.conf
	
	@echo [.] Adding machine path
	@echo '"machines":"$(machine_folder)",' >> $(config_folder)/htb.conf
	
	@echo [.] Adding config path
	@echo '"config":"$(config_folder)",' >> $(config_folder)/htb.conf
        
	@echo [.] Adding install path
	@echo '"install":"$(PWD)",' >> $(config_folder)/htb.conf
	
	@echo [.] Adding vpn config
	@echo '"vpnid":"0",' >> $(config_folder)/htb.conf
	
	@echo [.] Adding the memorization of last session
	@echo '"last":"",' >> $(config_folder)/htb.conf
	
	@echo [.] Adding OSCP Machines
	@echo '"OSCP":["Lame","Branfuck","Shocker","Bashed","Nibbles","Beep","Cronos","Nineveh","Sencse","Solidstate","Kotark","Node","Valentine","Poison","Sunday","Tartarsause","Legacy","Blue","Devel","Optimum","Bastard","Granny","Arctic","Grandpa","Silo","Bounty","Jerry"]' >> $(config_folder)/htb.conf
	
	@echo [+] DONE!
	@echo '}' >> $(config_folder)/htb.conf
	

install:
	@echo [+] Installing manager from $(PWD)
	ln -s $(PWD)/HTBManager2.0.py /usr/bin/HTBManager2.0

clean:
	rm /usr/bin/HTBmanager
	cd ~
	rm -rf /etc/HTB
