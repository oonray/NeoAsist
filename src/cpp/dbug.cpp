#include "../dbug.h"

std::string colors::red(std::string M)
{
    std::stringstream ss;
    ss << KRED << M << KNRM << " ";
    return ss.str();
}

std::string colors::green(std::string M)
{
    std::stringstream ss;
    ss << KGRN << M << KNRM << " ";
    return ss.str();
}

std::string colors::magenta(std::string M)
{
    std::stringstream ss;
    ss << KMAG << M << KNRM << " ";
    return ss.str();
}

void debug_t::debug(std::string M, std::string file, int line)
{
    std::cout << clr.magenta(KBUG) << "(" << file << ":" << line << ") " << M
              << '\n';
}

void debug_t::error(std::string M, std::string file, int line)
{
    std::cout << clr.red(KWAR) << "(" << file << ":" << line << ") " << M
              << '\n';
}

