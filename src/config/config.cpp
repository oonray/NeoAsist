#include "config.hpp"

ConfigFile::ConfigFile() {
    std::cout << "[Config] init" << '\n';
}

ConfigFile::~ConfigFile(){
}

void ConfigFile::prt_error(std::string M, std::string file, int line){
    std::cout << "[-][Config] error " << file << ' ' << line << ' ' << M << '\n';
}

int ConfigFile::Parse(std::string &filename){
    content = toml::parse_file(filename);
    if(!content.contains("target")){
        prt_error("No target spesified. Please specify a target.",__FILE__,__LINE__);
        return 1;
    }
    target = content["target"].as<toml::table>();
    if(!target->contains("ip")){
        prt_error("No target->ip spesified. Please specify a target->ip or target->ips.",__FILE__,__LINE__);
        return 1;
    }

    if(!target->contains("attacks")){
        prt_error("No Attack specified",__FILE__,__LINE__);
        return 1;
    }

    attacks = content["attacks"].as<toml::table>();
    return 0;
}


