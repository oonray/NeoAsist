#include "../factories.h"
//
// TARGET FACTORY
//
NeoA::Target_Factory_t::Target_Factory_t(Config_t* c) { config = c; }

int NeoA::Target_Factory_t::Create_all()
{
    auto content = config->Get_content();
    check_error(content->contains("target"), "No Tarets Specified.");
    for (toml::node& n : *(*content)["target"].as_array()) {
        result.push_back(this->Create(n));
    }
    return 0;
error:
    return 1;
}

NeoA::Target_t NeoA::Target_Factory_t::Create(toml::node& n)
{
    return Target_t(n.as_table());
}

std::vector<NeoA::Target_t> NeoA::Target_Factory_t::Get_Result()
{
    return result;
}

//
// ATTACK FACTORY
//

NeoA::Attack_Factory_t::Attack_Factory_t() {}

int NeoA::Attack_Factory_t::Create_all(Target_t& t)
{
    auto content = *t.get_node()->as_table();
    check_error(content.contains("attack"), "No Attacks Specified");
    for (toml::node& a : *content["attack"].as_array()) {
        result.push_back(this->Create(a));
    }
    return 0;
error:
    return 0;
}

NeoA::Attack_t NeoA::Attack_Factory_t::Create(toml::node& n)
{
    return NeoA::Attack_t(n.as_table());
}

//
// SERVICE FACTORY
//
NeoA::Service_Factory_t::Service_Factory_t() {}

