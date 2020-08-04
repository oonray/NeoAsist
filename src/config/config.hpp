#include <iostream>
#include <fstream>
#include <toml++/toml.h>
#include "../target/target.h"
#include "../debug/dbug.h"
#include <vector>

namespace NeoA {

class ConfigFile{
    private:
        std::string filename;
        toml::table content;
        std::vector<NeoA::Target_t> targets;

    public:
        ConfigFile(std::string f_name);
        ~ConfigFile();
        int Parse();
};

}

/**
 * ----------------
 *  TARGET
 * ----------------
 * [target]
 * ip="ip"
 * hostname="name"
 * [[target.service]]
 * type=ssh
 * port=22
 *
 * [[target.service]]
 * name=webserver01
 * type=apache
 * port=80
 *
 * [[attack]]
 * name="sqalmap"
 * type="sqlmap"
 * [want]
 * name="nothing found"
 * [got]
 * output=""
 *  # set by the program
 * [error]
 * exit=0
 * present=0
 *  # set by programm
 *
 * [[attack]]
 * name="necat"
 * type="custom"
 * shell="bash"
 * [command]
 * cmd="nc"
 * args=["-zv","{{target.ip}}","{{service[3].port}}"]
 * [want]
 * name="succeded"
 * [got]
 * output=""
 *  # set by the program
 * [error]
 * exit=0
 * present=0
 *  # set by programm
 */
