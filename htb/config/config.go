/*

@author oonray
@brief a module for interacting with the config

*/

package main

import (
    "os"
    "os/exec"
    "fmt"
    "encoding/json"
    "io/ioutil"
    dbg "github.com/oonray/godbg" // $GOPATH/src/github.com/oonray/godbg/dbg.go
)

const (
    config_path    = "/etc/htb"
    file    = ".htbrc"
)

var (
    home string
    Config config
    config_file string
)

type config struct {
    Machines          string       `json:"machines"`
    LastMachine       string       `json:"lastmachine"`
    OSCP_Machines     []string     `json:"oscpmachines"`
    API               Api          `json:"api"`
}

func init(){
    Config.OSCP_Machines = []string{"Lame", "Branfuck", "Shocker", "Bashed", "Nibbles", "Beep", "Cronos", "Nineveh", "Sencse", "Solidstate", "Kotark", "Node", "Valentine", "Poison", "Sunday", "Tartarsause", "Legacy", "Blue", "Devel", "Optimum", "Bastard", "Granny", "Arctic", "Grandpa", "Silo", "Bounty", "Jerry"}

    Config.API.Url = "https://hackthebox.eu/api"

    err := check_files()
    if err != nil {
        dbg.Log_info("Writing initial config")
        err = first_write()
        dbg.Check_error(err,"Could not Write to files!")
     }
    Load_config()
    Write_config()
}

func check_files() error {
    home = os.Getenv("HOME")
    _, err := os.Stat(fmt.Sprintf("%s/%s",home,file))
    if err != nil {
        _, err := os.Stat(fmt.Sprintf("%s/config",config_path))
        if err != nil {
            dbg.Log_error("There must be a config file @ /etc/htb")
            dbg.Log_info("Creating file @ /etc/htb")
            f, _ := os.Create(fmt.Sprintf("%s/config",config_path))
            defer f.Close()

            config_file = fmt.Sprintf("%s/config",config_path)
            return err
        }
        config_file = fmt.Sprintf("%s/config",config_path)
    } else {
        config_file = fmt.Sprintf("%s/%s",home,file)
    }
    return nil
}

func first_write() error {
    defer dbg.Rec()

    dbg.Log_info("Writing First Config file to /etc/HTB/config!")
    err := os.MkdirAll(config_path, os.ModePerm)
    if err != nil {return err}
    Write_config()
    return nil
}

func Load_config(){
    data, err := ioutil.ReadFile(config_file)
    dbg.Check_error(err, "Could not Read the Config File.")
    err = json.Unmarshal(data,&Config)
    dbg.Check_error(err, "Could not Parse the Config File.")
}

func Write_json(file string,data ) error {
    data, err := json.Marshal(Config)
    dbg.Check_error(err,"Could not parse Json")

    err = ioutil.WriteFile(file,data,0644)
    dbg.Check_error(err,"Could not write to file")
}

func Write_config() error {
    defer dbg.Rec()
    Write_json(confi_file)
    return nil
}

func Start_vpn() ([]byte,error) {
    dbg.Log_info("Starting VPN")
    cmd := exec.Command("/bin/sh", "-c", "sudo systemctl start HTB")
    return cmd.Output()
}

func Stop_vpn() ([]byte,error) {
    dbg.Log_info("Stop VPN")
    cmd := exec.Command("/bin/sh", "-c", "sudo systemctl stop HTB")
    return cmd.Output()
}

func Write_Machines(){
    defer dbg.Rec()
    
}
