/*
@author oonray @brief A program to manage HTB machines.

A program to manage HTB Machines.
The config is found int /etc/HTB
The config can be overrrided using a $(HOME)/.htbrc file
*/

package main

import (
    "fmt"
)

const (
    logpath = "/var/log/htb/"
    debug = false
)


func main() {
    Get_all_machines()
    fmt.Printf("%v\n",machines[0])
}
