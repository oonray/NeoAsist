#include "target.h"

NeoA::Target_t::Target_t(toml::table* t)
{
    node = t;

    hostname = *(*node)["hostname"].value<std::string>();
    ip = *(*node)["ip"].value<std::string>();
    for (toml::node& attack : *(*node)["attack"].as_array()) {
        attacks.push_back(NeoA::Attack_t(attack.as_table()));
    }
}

int NeoA::Target_t::attacks_n() { return attacks.size(); }
int NeoA::Target_t::services_n() { return services.size(); }
std::string NeoA::Target_t::ip_addr() { return ip; }
toml::node* NeoA::Target_t::get_node() { return node; }
