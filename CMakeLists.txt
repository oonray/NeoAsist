cmake_minimum_required(VERSION 3.9)

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

if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
  message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
  file(DOWNLOAD "https://raw.githubusercontent.com/conan-io/cmake-conan/master/conan.cmake"
          "${CMAKE_BINARY_DIR}/conan.cmake")
endif()

include(${CMAKE_BINARY_DIR}/conan.cmake)

conan_cmake_run(REQUIRES boost/1.74.0                 BASIC_SETUP)
conan_cmake_run(REQUIRES Catch2/2.6.0@catchorg/stable BASIC_SETUP)
conan_cmake_run(REQUIRES spdlog/1.8.2                 BASIC_SETUP)
conan_cmake_run(REQUIRES crow/1.0                     BASIC_SETUP)
conan_cmake_run(REQUIRES libpq/13.1                   BASIC_SETUP)

add_executable(NeoAsist
    src/main.cpp)

target_link_libraries(NeoAsist ${CONAN_LIBS})
