/*

@author oonray
@brief a module for interacting with the config

*/

package main

import (
	"fmt"
	"github.com/fatih/color"
	"log"
	"os"
)

const (
	path    = "/etc/htb"
	altpath = ".htbrc"
)

type Config struct {
	Key           string   `json:"key"`
	Machines      string   `json:"machines"`
	Install       string   `json:"install"`
	Vpnstarted    bool     `json:"vpnstart"`
	LastMachine   string   `json:"lastmachine"`
	OSCP_Machines []string `json:"oscpmachines"`
}

func create_config() (Config, error) {
	oscpmachines := []string{"Lame", "Branfuck", "Shocker", "Bashed", "Nibbles", "Beep", "Cronos", "Nineveh", "Sencse", "Solidstate", "Kotark", "Node", "Valentine", "Poison", "Sunday", "Tartarsause", "Legacy", "Blue", "Devel", "Optimum", "Bastard", "Granny", "Arctic", "Grandpa", "Silo", "Bounty", "Jerry"}

	err := os.MkdirAll(path, os.ModeDir)
	if err != nil {
		log.Fatal(fmt.Sprintf("%s Error %s\n", color.RedString("[!]"), err))
		return Config{}, err
	}
	conf := Config{}
	conf.OSCP_Machines = oscpmachines

	return conf, nil
}

func write_config(conf Config) error {
	return nil
}

func get_config() (Config, error) {
	return Config{}, nil
}

func add_key(key string, conf Config) error {
	return nil
}

func add_machines_folder(key string, conf Config) error {
	return nil
}

func add_install_folder(key string, conf Config) error {
	return nil
}

func set_vpn_started(conf Config) error {
	return nil
}

func set_vpn_stopped(conf Config) error {
	return nil
}

func set_last_machine(id string, conf Config) error {
	return nil
}
