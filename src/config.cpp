#include "config.h"

NeoA::Config_t::Config_t(std::string f_name) { this->filename = f_name; }

NeoA::Config_t::~Config_t() {}

toml::table *NeoA::Config_t::Get_content() { return content.as_table(); }

NeoA::Config_t *NeoA::Config_t::Parse()
{
    try {
        content = toml::parse_file(filename);
    }
    catch (int e) {
        log_error("Could not open File");
    }

    check_error(content.contains("target"), "No Target");
    check_error(!content.is_array_of_tables(),
                "Content does not contain propper targets.");
    return this;
error:
    return NULL;
}
