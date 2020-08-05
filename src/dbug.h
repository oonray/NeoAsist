#include <iostream>
#include <sstream>
#include <string>

#ifndef __dbg
#define __dbg

class colors {
private:
    static constexpr char KNRM[] = "\x1B[0m";
    static constexpr char KRED[] = "\x1B[31m";
    static constexpr char KGRN[] = "\x1B[32m";
    static constexpr char KYEL[] = "\x1B[33m";
    static constexpr char KBL[] = "\x1B[34m";
    static constexpr char KMAG[] = "\x1B[35m";
    static constexpr char KCYN[] = "\x1B[36m";
    static constexpr char KWHT[] = "\x1B[37m";

public:
    /**
     * @brief prints something in red
     *
     * @param M the thing to print
     *
     * @return a red string
     */
    std::string red(std::string M);

    /**
     * @brief prints something in green
     *
     * @param M message
     *
     * @return  a green string
     */
    std::string green(std::string M);

    /**
     * @brief prints something in magenta
     *
     * @param M message
     *
     * @return  a magenta string
     */
    std::string magenta(std::string M);
};

class debug_t {
private:
    const static constexpr char KNOK[] = "[+]";
    const static constexpr char KBUG[] = "[.]";
    const static constexpr char KWAR[] = "[!]";

public:
    /**
     * @brief prints debug
     *
     * @param M mesage
     * @param file the file name
     * @param line the file line
     */
    static void debug(std::string M, std::string file, int line);
    /**
     * @brief prints error message
     *
     * @param M message
     * @param file the file name
     * @param line the line number
     */
    static void error(std::string M, std::string file, int line);
};

static debug_t dbg;
static colors clr;

/**
 * @brief (Checks if A is an error) if goto error
 *
 * @param A The condition
 * @param M the message to print
 *
 */
#define check_error(A, M) \
    if (!(A)) {           \
        log_error(M);     \
        goto error;       \
    }

#define log_error(M) dbg.error(M, __FILE__, __LINE__)

#define log_debug(M) dbg.debug(M, __FILE__, __LINE__);
#endif
