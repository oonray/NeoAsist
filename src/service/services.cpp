#include "services.h"

NeoA::Service_t::Service_t(){}

NeoA::Service_t::~Service_t(){}

NeoA::Service_t::Service_t(toml::node& t){
    auto tb = *t.as<toml::table>();
    name = *tb["name"].value<std::string>();
    type = *tb["type"].value<std::string>();
}

