cmake_minimum_required(VERSION 3.1)

project(stringprinter CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library(stringprinter src/stringprinter.cpp)
target_link_libraries(stringprinter ${CONAN_LIBS})
