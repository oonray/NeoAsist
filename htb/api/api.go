/*

@author oonray
@brief functions (a *Api) (a *Api) for communicating with the api

*/

package api

import (
    "io/ioutil"
    "net/http"
    "encoding/json"
    "fmt"
    dbg "github.com/oonray/godbg" // $GOPATH/src/github.com/oonray/godbg/dbg.go
)

var    client   http.Client
var    machines []Machine

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

func (a *Api) make_url(path string) string{
    return fmt.Sprintf("%s/%s?api_token=%s",Config.API.Url,path,Config.API.Token)
}

func (a *Api) headders(){
}

func (a *Api) make_request(path string,r_type string) *http.Request {
    url := make_url(path)
    req, _ := http.NewRequest(r_type,url,nil)
    if r_type == "GET"{
        req.Header.Set("User-Agent","curl/7.65.1")
    }
    return req
}

func (a *Api) Get_all_machines(){
    defer dbg.Rec()
    resp, err := client.Do(make_request("machines/get/all","GET"))
    defer resp.Body.Close()

    data, err := ioutil.ReadAll(resp.Body)
    dbg.Check_error(err,"Could not read data form request.")

    err = json.Unmarshal(data,&machines)
    dbg.Check_error(err,"Could not parse Machine json")
}


