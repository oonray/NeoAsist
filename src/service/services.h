#include <iostream>
#include <toml++/toml.h>

namespace NeoA {

class Service_t {
private:
    std::string name;
    std::string type;
public:
    Service_t();
    Service_t(toml::node& t);
    ~Service_t();
};

}
