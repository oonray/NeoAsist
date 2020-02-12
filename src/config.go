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

func set_logging_file(path string) error {
    /*
        @brief sets the logging to file
        @param (string) path the path to log to
    */

    f, err := os.OpenFile(path, os.O_RDWR | os.O_CREATE | os.O_APPEND, 0666)
    if err != nil {
        log.Fatalf("error opening file: %v", err)
        return err
    }
    defer f.Close()
    log.SetOutput(f)
    return nil
}

func create_config() (Config, error) {
	/*
        @brief cretes the initial config file.
        
        Creates the initial config file.
        Sets the OSCP machnes.
        Writes the config.

    */
    
    oscpmachines := []string{"Lame", "Branfuck", "Shocker", "Bashed", "Nibbles", "Beep", "Cronos", "Nineveh", "Sencse", "Solidstate", "Kotark", "Node", "Valentine", "Poison", "Sunday", "Tartarsause", "Legacy", "Blue", "Devel", "Optimum", "Bastard", "Granny", "Arctic", "Grandpa", "Silo", "Bounty", "Jerry"}

	err := os.MkdirAll(path, os.ModeDir)
	if err != nil {
        log.Printf(fmt.Sprintf("%s Error crating config dir: %s\n", color.RedString("[!]"), err))
		return Config{}, err
	}
	
    err = os.MkdirAll(logpath, os.ModeDir)
	if err != nil {
        log.Printf(fmt.Sprintf("%s Error creating loging dir: %s\n", color.RedString("[!]"), err))
		return Config{}, err
	}
    log.Printf("%s Created %s folder",color.GreenString("[+]"),logpath)

	conf := Config{}
	conf.OSCP_Machines = oscpmachines
    log.Printf("%s Created config", color.GreenString("[+]"))
    
    err = write_config(conf)
    if err != nil {
        log.Printf("%s Could not write config",color.RedString("[!]"))
    }

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
