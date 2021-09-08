project(application)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(application src/main.cpp)
target_link_libraries(application ${CONAN_LIBS})

