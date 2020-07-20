package machines

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
