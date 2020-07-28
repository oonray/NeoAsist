#include <iostream>
#include <fstream>
#include "yaml-cpp/yaml.h"

class Config{
    private:
        YAML::Node document;
        YAML::NodeType::value Type();
    public:
        Config();
        ~Config();
        void Parse(std::string filename);
        int Size();
};

