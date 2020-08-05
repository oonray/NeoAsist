
#include <iostream>
#include "config.h"
#include "dbug.h"

NeoA::ConfigFile *cfg;

int main(void)
{
    log_debug("Starting");

    cfg = new NeoA::ConfigFile("/opt/git/NeoAsist/tests/config.toml");

    log_debug("Parsing");
    if (!cfg->Parse()) return 1;

    std::cout << "After Parse" << '\n';
    return 0;
}

