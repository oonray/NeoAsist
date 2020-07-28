cmake_minimum_required()
cmake_minimum_required(VERSION 3.2)

set(CMAKE_CXX_COMPILER_ID "GNU")
set(CMAKE_CXX_COMPILER "g++")
set(CMAKE_CXX_COMPILER_VERSION "8.3.0")
set(CMAKE_SYSTEM_NAME "Linux")

set(CMAKE_FIND_LIBRARY_PREFIXES "lib")
set(CMAKE_FIND_LIBRARY_SUFFIXES ".so;.a")

include(build/conanbuildinfo.cmake)
conan_basic_setup()

project(NeoAsist
    LANGUAGES CXX
    VERSION 1)

add_executable(NeoAsist 
    src/main.cpp
    src/config/config.cpp)

target_link_libraries(NeoAsist ${CONAN_LIBS})
