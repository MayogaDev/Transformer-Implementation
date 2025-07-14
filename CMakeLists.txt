cmake_minimum_required(VERSION 3.10)
project(FashionMNISTTransformer)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Set build type to Release for better performance
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# Compiler-specific options
if(MSVC)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /O2 /W3")
else()
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -Wall -Wextra")
endif()

# Include directories
include_directories(${CMAKE_SOURCE_DIR}/include)

# Source files
set(SOURCES
    src/matrix.cpp
    src/mnist_loader.cpp
    src/transformer.cpp
    main.cpp
)

# Create executable
add_executable(${PROJECT_NAME} ${SOURCES})

# Platform-specific settings
if(WIN32)
    # Windows-specific settings
    set_target_properties(${PROJECT_NAME} PROPERTIES
        WIN32_EXECUTABLE FALSE
    )
endif()

# Optional: Add OpenMP support for parallel processing
find_package(OpenMP)
if(OpenMP_CXX_FOUND)
    target_link_libraries(${PROJECT_NAME} OpenMP::OpenMP_CXX)
    message(STATUS "OpenMP found and will be used for parallel processing")
else()
    message(STATUS "OpenMP not found - continuing without parallel processing")
endif()

# Print build information
message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")
message(STATUS "C++ standard: ${CMAKE_CXX_STANDARD}")
message(STATUS "Compiler: ${CMAKE_CXX_COMPILER_ID}")
