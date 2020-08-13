cmake_minimum_required()
cmake_minimum_required(VERSION 3.2)

set(CMAKE_CXX_COMPILER_ID "GNU")
set(CMAKE_CXX_COMPILER "g++")
set(CMAKE_CXX_COMPILER_VERSION "8.3.0")
set(CMAKE_SYSTEM_NAME "Linux")

set(CMAKE_FIND_LIBRARY_PREFIXES "lib")
set(CMAKE_FIND_LIBRARY_SUFFIXES ".so;.a")

set(CMAKE_EXPORT_COMPILE_COMMANDS on)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


include(build/conanbuildinfo.cmake)
conan_basic_setup()


project(NeoAsist
    LANGUAGES CXX
    VERSION 1)

add_executable(NeoAsist 
    src/main.cpp
    src/config.cpp
    src/target.cpp
    src/services.cpp
    src/dbug.cpp
    src/attacks.cpp
    src/factories.cpp
    )


set(CMAKE_CXX_FLAGS "-std=c++2a ${CMAKE_CXX_FLAGS}")

target_link_libraries(NeoAsist ${CONAN_LIBS})

install(TARGETS NeoAsist DESTINATION bin)
