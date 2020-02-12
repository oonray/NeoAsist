package main

import (
	"crypto/sha512"
	"encoding/hex"
	"encoding/json"
	"github.com/fatih/color"
	"io/ioutil"
	"os"
    "log"
	"reflect"
	"testing"
    "strings"
)

var conf Config

func Test_create_config(t *testing.T) {
	oscpmachines := []string{"Lame", "Branfuck", "Shocker", "Bashed", "Nibbles", "Beep", "Cronos", "Nineveh", "Sencse", "Solidstate", "Kotark", "Node", "Valentine", "Poison", "Sunday", "Tartarsause", "Legacy", "Blue", "Devel", "Optimum", "Bastard", "Granny", "Arctic", "Grandpa", "Silo", "Bounty", "Jerry"}

	conf, err := create_config()
	if err != nil {
		t.Errorf("%s Function error %s ", color.RedString("[!]"), err)
	}

	if _, err := os.Stat(path); os.IsNotExist(err) {
		t.Errorf("%s Path %s not created by config", color.RedString("[!]"), err)
	}
	
    if _, err := os.Stat(logpath); os.IsNotExist(err) {
		t.Errorf("%s LogDir %s not created by config", color.RedString("[!]"), err)
	}

	file, err := os.Open(path + "/htb.conf")
	if err != nil {
		t.Errorf("%s File %s could not be opened after creation: %s", color.RedString("[!]"), path+"/htb.conf", err)
	}

	data, err := ioutil.ReadAll(file)
	if err != nil {
		t.Errorf("%s File contents could not be read %s", color.RedString("[!]"), err)
	}

	json.Unmarshal(data, &conf)
	if !reflect.DeepEqual(conf.OSCP_Machines, oscpmachines) {
		t.Errorf("%s The wrong values where written to OSCP_Machines", color.RedString("[!]"))
	}
}

func Test_set_logging_file(t *testing.T) {
    file := "/var/log/htb/testing.log"

    err := set_logging_file(file)
	if err != nil {
        t.Errorf("%s There was an error setting the log file: %s",color.RedString("[!]"),err)
    }

    hash := sha512.Sum512([]byte("Hello World"))
	key := hex.EncodeToString(hash[:]) 
    log.Printf("%s",key)
    
    f, err := os.Open(file)
    if err != nil {
        t.Errorf("%s Could not open file after logging.",color.RedString("[!]"))
    }

    data, err := ioutil.ReadAll(f)
    if err != nil {
        t.Errorf("%s Error reading file content after logging", color.RedString("[!]"))
    } 
    if !strings.Contains(string(data),key) {
        t.Errorf("%s The logg data is different form the data logged",color.RedString("[!]"))
    }
}

func Test_add_key(t *testing.T) {
	hash := sha512.Sum512([]byte("Hello World"))
	key := hex.EncodeToString(hash[:])

	err := add_key(key, conf)
	if err != nil {
		t.Errorf("%s add_key returned error %s", color.RedString("[!]"), err)
	}
	if conf.Key != key {
		t.Errorf("%s Wrong key in config after write", color.RedString("[!]"))
	}
}

func Test_add_machines_folder(t *testing.T) {
	hash := sha512.Sum512([]byte("/home/oonray/HTB"))
	key := hex.EncodeToString(hash[:])

	err := add_machines_folder(key, conf)
	if err != nil {
		t.Errorf("%s There was an error changing the machine folder %s", color.RedString("[!]"), err)
	}
	if conf.Machines != key {
		t.Errorf("%s The value of the machine folder is wrong after change", color.RedString("[!]"))
	}
}

func Test_add_install_folder(t *testing.T) {
	hash := sha512.Sum512([]byte("/opt/HTBManager"))
	key := hex.EncodeToString(hash[:])

	err := add_install_folder(key, conf)
	if err != nil {
		t.Errorf("%s There was an error changing the install folder %s", color.RedString("[!]"), err)
	}
	if conf.Install != key {
		t.Errorf("%s The value of the install folder is wrong after change", color.RedString("[!]"))
	}

}

func Test_set_vpn_started(t *testing.T) {
	err := set_vpn_started(conf)
	if err != nil {
		t.Errorf("%s There was an error setting VPN: %s", color.RedString("[!]"), err)
	}
	if conf.Vpnstarted != true {
		t.Errorf("%s VPN no set to started", color.RedString("[!]"))
	}
}

func Test_set_vpn_stopped(t *testing.T) {
	err := set_vpn_stopped(conf)
	if err != nil {
		t.Errorf("%s There was an error setting VPN: %s", color.RedString("[!]"), err)
	}
	if conf.Vpnstarted != false {
		t.Errorf("%s VPN no set to stopped", color.RedString("[!]"))
	}

}

func Test_set_last_machine(t *testing.T) {
	err := set_last_machine("Jerry", conf)
	if err != nil {
		t.Errorf("%s There was an error setting VPN: %s", color.RedString("[!]"), err)
	}
	if conf.LastMachine != "Jerry" {
		t.Errorf("%s The value of Last machine was wrong after setting", color.RedString("[!]"))
	}
}

func Test_write_config(t *testing.T) {
	var check Config

	err := write_config(conf)
	if err != nil {
		t.Errorf("%s Could not write config: %s", color.RedString("[!]"), err)
	}

	file, err := os.Open(path + "/htb.conf")
	if err != nil {
		t.Errorf("%s File open Error after write: %s", color.RedString("[!]"), err)
	}

	data, err := ioutil.ReadAll(file)
	if err != nil {
		t.Errorf("%s File read error after write: %s", color.RedString("[!]"), err)
	}
	json.Unmarshal(data, &check)
	if !reflect.DeepEqual(check, conf) {
		t.Errorf("%s Values not correct after write", color.RedString("[!]"))
	}

}
func Test_get_config(t *testing.T) {
	check, err := get_config()
	if err != nil {
		t.Errorf("%s Could not get config: %s", color.RedString("[!]"), err)
	}
	if !reflect.DeepEqual(check, conf) {
		t.Errorf("%s Conf has wrong values when read", color.RedString("[!]"))
	}
}
