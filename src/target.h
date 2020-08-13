#include <toml++/toml.h>
#include <iostream>

#ifndef __target_h
#define __target_h

#include "attacks.h"
#include "services.h"
#include "target.h"

namespace NeoA {

class Target_t {
private:
    toml::table* node;
    std::string ip;
    std::string hostname;
    std::vector<Service_t> services;
    std::vector<Attack_t> attacks;

public:
    Target_t(toml::table* t);
    int attacks_n();
    int services_n();
    std::string ip_addr();
    toml::node* get_node();
    void operator+(Attack_t& a);
    void operator+(Service_t& s);
    void operator-(Attack_t& a);
    void operator-(Service_t& s);
};

}  // namespace NeoA

#endif
