cmake_minimum_required()
cmake_minimum_required(VERSION 3.2)

set(CMAKE_EXPORT_COMPILE_COMMANDS on)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

set(CMAKE_CXX_FLAGS "-Wall -Wextra")
set(CMAKE_CXX_FLAGS_DEBUG "-g")
set(CMAKE_CXX_FLAGS_RELEASE "-O3")

project(NeoAsist
    LANGUAGES CXX
    VERSION 1)

include(build/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(NeoAsist 
    src/main.cpp
    src/cpp/config.cpp
    src/cpp/target.cpp
    src/cpp/services.cpp
    src/cpp/dbug.cpp
    src/cpp/attacks.cpp
    src/cpp/factories.cpp
    )


set(CMAKE_CXX_FLAGS "-std=c++2a ${CMAKE_CXX_FLAGS}")

target_link_libraries(NeoAsist ${CONAN_LIBS})

install(TARGETS NeoAsist DESTINATION bin)
