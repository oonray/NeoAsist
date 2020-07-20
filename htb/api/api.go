/*

@author oonray
@brief functions for communicating with the api

*/

package main

import (
    "io/ioutil"
    "net/http"
    "encoding/json"
    "fmt"
    dbg "github.com/oonray/godbg" // $GOPATH/src/github.com/oonray/godbg/dbg.go
)

var    client   http.Client
var    machines []Machine

/*

  {
    "id": 262,
    "name": "SneakyMailer",
    "os": "Linux",
    "ip": "10.10.10.197",
    "avatar_thumb": "https://www.hackthebox.eu/storage/avatars/5f5ab2f3fb31673d80623bdd98b286c3_thumb.png",
    "points": 30,
    "release": "2020-07-11",
    "retired_date": null,
    "maker": {
      "id": 106709,
      "name": "sulcud"
    },
    "maker2": null,
    "rating": "3.5",
    "user_owns": 427,
    "root_owns": 422,
    "retired": false,
    "free": true
  }
*/


type Api struct {
    Url     string  `json:"url"`
    Token   string  `json:"token"`
}

type Machine struct {
    Id          int         `json:"id"`
    Name        string      `json:"name"`
    Os          string      `json:"os"`
    Ip          string      `json:"ip"`
    Points      int         `json:"points"`
    Rating      string      `json:"rating"`
    User_owns   int         `json:"user_owns"`
    Root_owns   int         `json:"root_owns"`
    Retired     bool        `json:"retired"`
}

func init(){
    client = http.Client{}
}

func make_url(path string) string{
    return fmt.Sprintf("%s/%s?api_token=%s",Config.API.Url,path,Config.API.Token)
}

func headders(){
}

func make_request(path string,r_type string) *http.Request {
    url := make_url(path)
    req, _ := http.NewRequest(r_type,url,nil)
    if r_type == "GET"{
        req.Header.Set("User-Agent","curl/7.65.1")
    }
    return req
}

func Get_all_machines(){
    defer dbg.Rec()
    resp, err := client.Do(make_request("machines/get/all","GET"))
    defer resp.Body.Close()

    data, err := ioutil.ReadAll(resp.Body)
    dbg.Check_error(err,"Could not read data form request.")

    err = json.Unmarshal(data,&machines)
    dbg.Check_error(err,"Could not parse Machine json")
}


