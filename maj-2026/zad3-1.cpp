#include <iostream>
#include <cmath>
#include <fstream>
#include <sstream>

int asciiDif(std::string word1, std::string word2) {
    int sum1 = 0, sum2 = 0;
    for (char c : word1) {
        sum1 += c;
    }
    for (char c : word2) {
        sum2 += c;
    }

    return std::abs(sum1 - sum2);
}

int main() {
    std::ifstream pairsFile("dane/pary.txt");
    std::string line;

    int largestDif = 0;
    while (std::getline(pairsFile, line)) {
        std::istringstream iss(line);
        std::string word1, word2;
        iss >> word1 >> word2;
 
        int dif = asciiDif(word1, word2);
        if (dif > largestDif) largestDif = dif;
    }

    pairsFile.close();
    std::cout << largestDif << std::endl;
}