
cmake_minimum_required(VERSION 3.20)

project(HelloC LANGUAGES C)

set(CMAKE_C_STANDARD 17)
set(CMAKE_C_STANDARD_REQUIRED ON)

add_executable(HelloC main.c)
