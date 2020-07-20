/*

@author oonray
@brief functions (a *Api) (a *Api) for communicating with the api

*/

package api

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"time"

	dbg "github.com/oonray/godbg" // $GOPATH/src/github.com/oonray/godbg/dbg.go
)

var    client   http.Client

type Api struct {
    Url         string      `json:"url"`
    Token       string      `json:"token"`
    Update      string      `json:"update"`
    Machines    []Machine    `json:"machines"`
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
    return fmt.Sprintf("%s/%s?api_token=%s",a.Url,path,a.Token)
}

func (a *Api) headders(){
}

func (a *Api) make_request(path string,r_type string) *http.Request {
    url := a.make_url(path)
    req, _ := http.NewRequest(r_type,url,nil)
    if r_type == "GET"{
        req.Header.Set("User-Agent","curl/7.65.1")
    }
    return req
}

func (a *Api) get_all_machines(){
    defer dbg.Rec()
    resp, err := client.Do(a.make_request("machines/get/all","GET"))
    dbg.Check_error(err,"Could not get data")
    defer resp.Body.Close()

    data, err := ioutil.ReadAll(resp.Body)
    dbg.Check_error(err,"Could not read data form request.")

    err = json.Unmarshal(data,&a.Machines)
    dbg.Check_error(err,"Could not parse Machine json")
}

func (a *Api) Get_Machine(name string) *Machine {
    defer dbg.Rec()
    for _, machine := range a.Machines {
        if machine.Name == name {
            return &machine
        }
    }
    return nil
}

func (a *Api) Update_Machines(){
    defer dbg.Rec()
    a.get_all_machines()

    now := time.Now()
    data, err := now.MarshalJSON()
    a.Update = string(data)
    dbg.Check_error(err,"Could not Update Machined")
}

func (a *Api) Check_Update(){
    var then time.Time

    now := time.Now()
    then.UnmarshalJSON([]byte(a.Update))
    dt := now.Sub(then)

    if dt.Hours() >= 24.0 {
        a.Update_Machines()
    }
}
