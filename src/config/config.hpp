#include <iostream>
#include <fstream>
#include <toml++/toml.h>


class ConfigFile{
    private:
        toml::table content;
        toml::table *target;
        toml::table *attacks;

    public:
        ConfigFile();
        ~ConfigFile();
        void prt_error(std::string M,std::string file,int line);
        int Parse(std::string &filename);
};


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
