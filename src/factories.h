
#include "config.h"
#include "target.h"

namespace NeoA {

class Attack_Factory_t {
private:
    std::vector<Attack_t> result;

public:
    Attack_Factory_t();
    Attack_t Create(toml::node &n);
    int Create_all(Target_t &t);
};

class Service_Factory_t {
private:
    std::vector<Service_t> result;

public:
    Service_Factory_t();
    Service_t Create(toml::node &n);
    int Create_all(Target_t &t);
};

class Target_Factory_t {
private:
    Attack_Factory_t Attack_factory;
    Service_Factory_t Service_factory;
    Config_t *config;
    std::vector<Target_t> result;

public:
    Target_Factory_t(Config_t *c);
    ~Target_Factory_t();

    Target_t Create(toml::node &n);
    int Create_all();
    std::vector<Target_t> Get_Result();
};

}  // namespace NeoA
