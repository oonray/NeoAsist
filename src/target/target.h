#include <iostream>
#include <toml++/toml.h>
#include "../service/services.h"

namespace NeoA {

class Target_t {
    private:
        std::string ip;
        std::string hostname;
        std::vector<Service_t> services;
    public:
        Target_t(toml::node& t); 
};

}
