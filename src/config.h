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
    Config_t *Parse();
    toml::table *Get_content();
};

}  // namespace NeoA

