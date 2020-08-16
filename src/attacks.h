#include <toml++/toml.h>
#include <iostream>
#include <sstream>
#include <vector>

#ifndef __attack_h
#define __attack_h

namespace NeoA {

class Attack_t {
private:
    std::string name;
    std::string binary;
    std::string proto;
    std::vector<std::string> args;
    int run;

public:
    Attack_t();
    Attack_t(toml::table* n);
    Attack_t(std::string name, std::string binary, std::string proto,
             std::vector<std::string> args);

    std::string get_binary() const;
    std::string get_proto() const;
    std::string get_name() const;
    std::vector<std::string> get_args() const;

    int Run();
    std::string command();
};

}  // namespace NeoA

#endif
