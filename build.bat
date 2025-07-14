@echo off
echo ===================================
echo Fashion-MNIST Transformer Build Script
echo ===================================

REM Create build directory
if not exist "build" mkdir build
cd build

echo Configuring project with CMake...
cmake .. -G "Visual Studio 16 2019" -A x64

if %ERRORLEVEL% neq 0 (
    echo CMake configuration failed!
    echo Trying with different generator...
    cmake .. -G "MinGW Makefiles"
    if %ERRORLEVEL% neq 0 (
        echo CMake configuration failed with both generators!
        echo Please ensure you have CMake and a C++ compiler installed.
        pause
        exit /b 1
    )
)

echo Building project...
cmake --build . --config Release

if %ERRORLEVEL% neq 0 (
    echo Build failed!
    pause
    exit /b 1
)

echo.
echo ===================================
echo Build completed successfully!
echo ===================================
echo.
echo To run the program:
echo   cd build
echo   .\Release\FashionMNISTTransformer.exe
echo.
echo Or run from Debug folder if built in Debug mode:
echo   .\Debug\FashionMNISTTransformer.exe
echo.

pause
