#include <toml++/toml.h>
#include <iostream>
#include <vector>

#ifndef __attack_h
#define __attack_h

namespace NeoA {

class Attack_t {
private:
    std::string name;
    std::string command;
    std::string binary;
    std::vector<std::string> args;
    int run;

public:
    Attack_t();
    Attack_t(toml::table* n);
    int Run();
};

class Nmap_t : public Attack_t {
private:
public:
    Nmap_t();
    Nmap_t(toml::node* n);
    Nmap_t(Attack_t* a);
};

}  // namespace NeoA

#endif
