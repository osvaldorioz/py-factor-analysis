cmake_minimum_required(VERSION 3.12)

project(fa_module)
set(CMAKE_CXX_STANDARD 11)
set(PYBIND11_PYTHON_VERSION 3.12)
set(CMAKE_CXX_FLAGS "-O2 -Ofast -Wall -shared -std=c++20 -fPIC")

find_package(pybind11 REQUIRED)

pybind11_add_module(${PROJECT_NAME} app/factor_analysis.cpp)

target_compile_definitions(${PROJECT_NAME} PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
target_include_directories(${PROJECT_NAME} PRIVATE ${PYBIND11_INCLUDE_DIRS})

