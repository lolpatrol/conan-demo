project(project)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(project src/main.cpp)
target_link_libraries(project ${CONAN_LIBS})

