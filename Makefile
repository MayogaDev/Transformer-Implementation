# Simple Makefile for Fashion-MNIST Transformer
# Alternative to CMake for simple compilation

CXX = g++
CXXFLAGS = -std=c++17 -O3 -Wall -Wextra
INCLUDES = -Iinclude
TARGET = FashionMNISTTransformer
SRCDIR = src
SOURCES = $(SRCDIR)/matrix.cpp $(SRCDIR)/mnist_loader.cpp $(SRCDIR)/transformer.cpp main.cpp
OBJECTS = $(SOURCES:.cpp=.o)

# Default target
all: $(TARGET)

# Build target
$(TARGET): $(OBJECTS)
	$(CXX) $(OBJECTS) -o $(TARGET)
	@echo "Build completed! Run with: ./$(TARGET)"

# Compile source files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

# Clean build files
clean:
	rm -f $(OBJECTS) $(TARGET)
	@echo "Clean completed!"

# Clean and rebuild
rebuild: clean all

# Install dependencies (Linux/macOS)
install-deps:
	@echo "Installing build dependencies..."
	@if command -v apt-get >/dev/null 2>&1; then \
		sudo apt-get update && sudo apt-get install -y build-essential cmake; \
	elif command -v yum >/dev/null 2>&1; then \
		sudo yum groupinstall -y "Development Tools" && sudo yum install -y cmake; \
	elif command -v brew >/dev/null 2>&1; then \
		brew install cmake; \
	else \
		echo "Please install build tools manually"; \
	fi

# Show help
help:
	@echo "Available targets:"
	@echo "  all        - Build the project (default)"
	@echo "  clean      - Remove build files"
	@echo "  rebuild    - Clean and build"
	@echo "  install-deps - Install build dependencies"
	@echo "  help       - Show this help message"

.PHONY: all clean rebuild install-deps help
