#include "../attacks.h"

NeoA::Attack_t::Attack_t(toml::table* n)
{
    // TODO: Implement Attack
}

NeoA::Attack_t::Attack_t()
    : name("nmap"),
      binary("nmap"),
      proto("tcp"),
      args({"-sV", "-sC", "-p-", "-o"})
{
}

std::string NeoA::Attack_t::command()
{
    std::ostringstream os;
    os << binary << ' ';
    for (std::string ar : args) {
        if (ar == "-o") {
            os << ar << ' ' << name << '_' << proto;
        }
        os << ar << ' ';
    }
    return os.str();
}

std::ostream& operator<<(std::ostream& st, NeoA::Attack_t& a)
{
    return st << a.command();
}
