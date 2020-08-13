#include <toml++/toml.h>
#include <iostream>

#ifndef __service_h
#define __service_h

namespace NeoA {

class Service_t {
private:
    std::string name;
    std::string type;

public:
    Service_t();
    Service_t(toml::node& t);
    ~Service_t();
    int Attack();
};

class Webserver_t : public Service_t {
public:
private:
};

}  // namespace NeoA

#endif
