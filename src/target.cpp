#include "target.h"

NeoA::Target_t::Target_t(toml::node& t)
{
    toml::table* data = t.as_table();

    hostname = *(*data)["hostname"].value<std::string>();
    ip = *(*data)["ip"].value<std::string>();
}

