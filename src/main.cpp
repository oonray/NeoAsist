#include <iostream>
#include "config/config.hpp"

ConfigFile *cfg;

int main(void){
    std::string filename = "/opt/git/NeoAsist/tests/config.toml";

    cfg = new ConfigFile();
    if(cfg->Parse(filename) != 0)
        return 1;

    std::cout << "After Parse" << '\n';
    return 0;
}


