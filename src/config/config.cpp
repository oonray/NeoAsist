#include "config.hpp"

Config::Config(){
}

Config::~Config(){
}

/**
 * @brief Gets the content of a file and makes it avaliable in Config.
 * @param std::string filename The filename of the file to parse
 */
void Config::Parse(std::string filename){
//    auto data = YAML::Load(filename);
  //  if(data.Type() != YAML::NodeType::Undefined){
     //   document = data;
   // }
    //else{
   //     document = NULL;
    //}
}

/**
 * @brief Retuns size of the document or 0
 * @returns size of documentt
 */
int Config::Size(){
    return document.size();
}

/**
 * @brief Returns document node type
 */
YAML::NodeType::value Config::Type(){
    return document.Type();
}





