#include <iostream>
#include <string>
#include <sstream>

#ifndef __dbg
#define __dbg

class colors {
    private:
        static constexpr char KNRM[] =  "\x1B[0m";
        static constexpr char KRED[] =  "\x1B[31m";
        static constexpr char KGRN[] =  "\x1B[32m";
        static constexpr char KYEL[] =  "\x1B[33m";
        static constexpr char KBL[] =  "\x1B[34m";
        static constexpr char KMAG[] =  "\x1B[35m";
        static constexpr char KCYN[] =  "\x1B[36m";
        static constexpr char KWHT[] =  "\x1B[37m";
    public:
        std::string red(std::string M);
        std::string green(std::string M);
        std::string magenta(std::string M);
};

class debug_t {
    private:
        const static constexpr char KNOK[] = "[+]";
        const static constexpr char KBUG[] = "[.]";
        const static constexpr char KWAR[] = "[!]";
    public:
       static void debug(std::string M,std::string file,int line);
       static void error(std::string M, std::string file,int line);
};

static debug_t dbg;
static colors clr;

#define check_error(A, M) if(!(A)) { log_error(M);goto error; }
#define log_error(M) dbg.error(M,__FILE__,__LINE__)

#define log_debug(M) dbg.debug(M,__FILE__,__LINE__);
#endif
