#include "config.hpp"

NeoA::ConfigFile::ConfigFile(std::string f_name) {
    this->filename = f_name;
}

NeoA::ConfigFile::~ConfigFile(){
}

int NeoA::ConfigFile::Parse(){
    try{
        content = toml::parse_file(filename);
    } catch(int e) {
        log_error("Could not open File");
    }

    check_error(content.contains("target"),"No Target");
    //check_error(content.is_array_of_tables(),"Content does not contain propper targets.");
    for(toml::node& data : *content["target"].as_array()){
        toml::table tbl =  *data.as<toml::table>();
        for(toml::node& attack : *tbl["attack"].as_array()){
            toml::table tbl2 = *attack.as<toml::table>();
            std::cout << "Running attack: " << tbl2["name"] << " on " << tbl["ip"]  << '\n';
        }
    }

    log_debug("For Ending");
    return 0;

error:
    return 1;
}
