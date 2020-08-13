
#include <iostream>
#include "dbug.h"
#include "factories.h"

NeoA::Target_Factory_t *tf;
NeoA::Config_t *cf;

std::vector<NeoA::Target_t> targets;

int main(void)
{
    log_debug("Starting");
    cf = new NeoA::Config_t("/opt/git/NeoAsist/tests/config.toml");

    tf = new NeoA::Target_Factory_t(cf);

    tf->Create_all();

    targets = tf->Get_Result();

    std::cout << targets.size() << " targes" << '\t';
    return 0;
}

