#include <toml++/toml.h>
#include <fstream>
#include <iostream>
#include <vector>
#include "dbug.h"
#include "target.h"

namespace NeoA {

class Config_t {
private:
    std::string filename;
    toml::table content;

public:
    Config_t(std::string f_name);
    ~Config_t();
    int Parse();
    toml::table *Get_content();
};

class Config_Target_t : Config_t {
public:
    int Parse();
};

class Config_Attack_t : Config_t {
};

class Config_Services_t : Config_t {
};

}  // namespace NeoA

