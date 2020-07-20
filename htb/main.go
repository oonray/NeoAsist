/*
@author oonray @brief A program to manage HTB machines.

A program to manage HTB Machines.
The config is found int /etc/HTB
The config can be overrrided using a $(HOME)/.htbrc file
*/

package main

import (
	"NeoAsist/htb/config"
	"fmt"
)

func main() {
    config.Configuration.API.Update_Machines()
    config.Configuration.Write_config()
    machine := config.Configuration.API.Get_Machine("Lame")
    fmt.Printf("%v\n",machine)
}
