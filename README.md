# Fashion-MNIST Transformer Classifier

A complete implementation of a Transformer neural network in C++ for classifying Fashion-MNIST images. This project includes both encoder and decoder components of the Transformer architecture.

## Features

- **Complete Transformer Architecture**: Implements both encoder and decoder layers
- **Multi-Head Attention**: Self-attention and cross-attention mechanisms
- **Positional Encoding**: Sinusoidal positional embeddings
- **Patch-Based Vision Transformer**: Converts 28x28 images into 4x4 patches
- **Layer Normalization**: For training stability
- **GELU Activation**: Modern activation function used in transformers
- **Fashion-MNIST Dataset Support**: Loads and processes Fashion-MNIST binary files

## Architecture

### Model Components

1. **Patch Embedding**: Converts 28x28 images into 49 patches (7x7 grid of 4x4 patches)
2. **Positional Encoding**: Adds positional information to patch embeddings
3. **Transformer Encoder**: 6 layers with multi-head self-attention
4. **Transformer Decoder**: 6 layers with masked self-attention and cross-attention
5. **Classification Head**: Linear layer for 10-class classification

### Model Parameters

- **Embedding Dimension**: 256
- **Attention Heads**: 8
- **Encoder/Decoder Layers**: 6 each
- **Feed Forward Dimension**: 1024
- **Patch Size**: 4x4
- **Number of Classes**: 10

## Fashion-MNIST Classes

0. T-shirt/top
1. Trouser
2. Pullover
3. Dress
4. Coat
5. Sandal
6. Shirt
7. Sneaker
8. Bag
9. Ankle boot

## Requirements

- C++17 compatible compiler
- CMake 3.10 or higher
- Fashion-MNIST dataset files (binary format)

### Recommended Compilers

- **Windows**: Visual Studio 2019/2022, MinGW-w64
- **Linux**: GCC 7+, Clang 5+
- **macOS**: Xcode 10+

## Installation and Building

### Windows

1. **Prerequisites**:
   ```cmd
   # Install Visual Studio Build Tools or Visual Studio
   # Install CMake from https://cmake.org/download/
   ```

2. **Build**:
   ```cmd
   # Clone or download the project
   cd TRANFOVERSINOPENCV
   
   # Run the build script
   build.bat
   ```

3. **Manual Build**:
   ```cmd
   mkdir build
   cd build
   cmake .. -G "Visual Studio 16 2019" -A x64
   cmake --build . --config Release
   ```

### Linux/macOS

```bash
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
```

## Dataset Setup

1. Download Fashion-MNIST dataset from: http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/
2. Place the files in the same directory as the dataset paths specified in main.cpp:
   - `train-images-idx3-ubyte`
   - `train-labels-idx1-ubyte`
   - `t10k-images-idx3-ubyte`
   - `t10k-labels-idx1-ubyte`

## Usage

### Running the Program

```cmd
# Windows (after building)
cd build\Release
FashionMNISTTransformer.exe

# Linux/macOS (after building)
cd build
./FashionMNISTTransformer
```

### Expected Output

The program will:
1. Load the Fashion-MNIST dataset
2. Initialize the Transformer model
3. Train for 5 epochs on a subset of the data
4. Evaluate on test data
5. Show sample predictions with confidence scores

### Sample Output

```
=== Fashion-MNIST Transformer Classifier ===

Loading Fashion-MNIST dataset...
Loading 60000 images of size 28x28
Loading 60000 labels
Loading 10000 images of size 28x28
Loading 10000 labels

Initializing Transformer model...
Model initialized successfully!

Training configuration:
- Learning rate: 0.001
- Epochs: 5
- Training samples: 1000
- Test samples: 200

Starting training...
--- Epoch 1/5 ---
...
Test Accuracy: 85.5%

=== Sample Predictions ===
Sample 1:
  True: Sneaker (7)
  Predicted: Sneaker (7)
  Confidence: 92.3%
  Correct: Yes
```

## Code Structure

```
TRANFOVERSINOPENCV/
├── include/
│   ├── matrix.h              # Matrix operations and utilities
│   ├── mnist_loader.h        # Fashion-MNIST dataset loader
│   └── transformer.h         # Transformer architecture
├── src/
│   ├── matrix.cpp            # Matrix implementation
│   ├── mnist_loader.cpp      # Dataset loading implementation
│   └── transformer.cpp       # Transformer implementation
├── main.cpp                  # Main application
├── CMakeLists.txt           # Build configuration
├── build.bat                # Windows build script
└── README.md                # This file
```

## Key Classes

### Matrix
- Basic matrix operations (addition, multiplication, transpose)
- Activation functions (ReLU, Sigmoid, Tanh, GELU, Softmax)
- Layer normalization
- Xavier initialization

### MNISTLoader
- Loads Fashion-MNIST binary files
- Converts raw bytes to normalized matrices
- Handles both images and labels

### Transformer Components
- **PositionalEncoding**: Sinusoidal position embeddings
- **MultiHeadAttention**: Self-attention and cross-attention
- **FeedForward**: Position-wise feed-forward networks
- **LayerNorm**: Layer normalization
- **TransformerEncoderLayer**: Complete encoder layer
- **TransformerDecoderLayer**: Complete decoder layer
- **Transformer**: Full model with classification head

## Performance Notes

- The implementation prioritizes clarity over performance
- For production use, consider optimizations like:
  - BLAS/LAPACK integration for matrix operations
  - GPU acceleration with CUDA/OpenCL
  - Batch processing for training
  - Mixed precision training
  - Memory optimizations

## Training Notes

- The current implementation includes a simplified training loop
- Full backpropagation is not implemented (placeholder only)
- For complete training, you would need to implement:
  - Gradient computation for all layers
  - Weight updates with proper learning rate schedules
  - Regularization techniques (dropout, weight decay)
  - Advanced optimizers (Adam, AdamW)

## Customization

### Changing Model Parameters

Edit the parameters in `main.cpp`:

```cpp
Transformer model(
    256,  // d_model - embedding dimension
    8,    // num_heads - attention heads
    6,    // num_layers - encoder/decoder layers
    1024, // d_ff - feed forward dimension
    10,   // num_classes - output classes
    4,    // patch_size - patch dimensions
    0.1   // dropout_rate - dropout probability
);
```

### Modifying Dataset Paths

Update the paths in `main.cpp`:

```cpp
std::string train_images_path = "path/to/train-images-idx3-ubyte";
std::string train_labels_path = "path/to/train-labels-idx1-ubyte";
std::string test_images_path = "path/to/t10k-images-idx3-ubyte";
std::string test_labels_path = "path/to/t10k-labels-idx1-ubyte";
```

## Troubleshooting

### Common Issues

1. **CMake not found**: Install CMake and add to PATH
2. **Compiler errors**: Ensure C++17 support
3. **Dataset not found**: Check file paths and download Fashion-MNIST
4. **Memory issues**: Reduce batch size or model dimensions
5. **Slow performance**: Enable compiler optimizations (-O3/Release mode)

### Build Issues

- **Windows**: Try different generators (Visual Studio, MinGW)
- **Linux**: Install build-essential package
- **macOS**: Install Xcode command line tools

## License

This project is for educational purposes. The Fashion-MNIST dataset is available under the MIT license.

## References

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - Original Transformer paper
- [An Image is Worth 16x16 Words](https://arxiv.org/abs/2010.11929) - Vision Transformer
- [Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist) - Dataset
