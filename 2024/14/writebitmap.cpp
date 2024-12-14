#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <stdint.h>

#pragma pack(push, 1)
struct BMPHeader {
    uint16_t fileType{0x4D42};  // 'BM'
    uint32_t fileSize{0};       // Size of the file
    uint16_t reserved1{0};
    uint16_t reserved2{0};
    uint32_t offsetData{54};    // Offset to the pixel data
};

struct DIBHeader {
    uint32_t size{40};          // Header size
    int32_t width{0};           // Image width
    int32_t height{0};          // Image height (negative for top-down)
    uint16_t planes{1};         // Number of planes
    uint16_t bitCount{24};      // Bits per pixel (24 for RGB)
    uint32_t compression{0};    // No compression
    uint32_t imageSize{0};      // Image size (can be 0 for uncompressed)
    int32_t xPixelsPerMeter{0};
    int32_t yPixelsPerMeter{0};
    uint32_t colorsUsed{0};
    uint32_t importantColors{0};
};
#pragma pack(pop)

void writeBitmap(const std::string& filename, const std::vector<std::string>& data) {
    int height = data.size();
    int width = height > 0 ? data[0].size() : 0;
    int padding = (4 - (width * 3) % 4) % 4;

    BMPHeader bmpHeader;
    DIBHeader dibHeader;
    dibHeader.width = width;
    dibHeader.height = -height; // Top-down
    dibHeader.imageSize = (width * 3 + padding) * height;
    bmpHeader.fileSize = sizeof(BMPHeader) + sizeof(DIBHeader) + dibHeader.imageSize;

    std::ofstream outFile(filename, std::ios::binary);
    if (!outFile) {
        std::cerr << "Error: Unable to create file " << filename << std::endl;
        return;
    }

    outFile.write(reinterpret_cast<const char*>(&bmpHeader), sizeof(bmpHeader));
    outFile.write(reinterpret_cast<const char*>(&dibHeader), sizeof(dibHeader));

    for (const auto& row : data) {
        for (char ch : row) {
            uint8_t color = (ch == '.') ? 0 : 255; // '.' is black, ' ' is white
            uint8_t pixel[] = {color, color, color}; // RGB
            outFile.write(reinterpret_cast<const char*>(pixel), sizeof(pixel));
        }
        // Add padding
        uint8_t pad[3] = {0, 0, 0};
        outFile.write(reinterpret_cast<const char*>(pad), padding);
    }

    outFile.close();
    std::cout << "Bitmap saved as " << filename << std::endl;
}

std::vector<std::string> readTextFile(const std::string& filename) {
    std::ifstream inFile(filename);
    if (!inFile) {
        std::cerr << "Error: Unable to open file " << filename << std::endl;
        return {};
    }

    std::vector<std::string> data;
    std::string line;
    while (std::getline(inFile, line)) {
        data.push_back(line);
    }
    return data;
}


std::string getOutputFilename(const std::string& inputFilename) {
    size_t dotPos = inputFilename.find_last_of('.');
    return inputFilename.substr(0, dotPos) + ".bmp";
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <input_text_file>" << std::endl;
        return 1;
    }

    std::string inputFile = argv[1];
    std::vector<std::string> textData = readTextFile(inputFile);

    if (textData.empty()) {
        std::cerr << "Error: No data read from file." << std::endl;
        return 1;
    }

    std::string outputFile = getOutputFilename(inputFile);
    writeBitmap(outputFile, textData);

    return 0;
}


