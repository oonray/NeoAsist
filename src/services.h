#include <toml++/toml.h>
#include <iostream>

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

}  // namespace NeoA
