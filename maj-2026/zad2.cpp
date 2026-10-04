#include <iostream>

int addition(int a, int b) {
    int carryCount = 0;
    bool isCarried = false;

    while (a / 10 != 0) {
        if (a % 10 + b % 10 + isCarried > 9) {
            carryCount++;
            isCarried = true;
        }
        else isCarried = false;
            
        a /= 10;
        b /= 10;
    }

    if (a + b + isCarried > 9) carryCount++;
    return carryCount;
}

int main() {
    std::cout << addition(27732, 72619) << std::endl;
    std::cout << addition(37932, 12528) << std::endl;
    std::cout << addition(88765, 11111) << std::endl;
    std::cout << addition(456789, 222222) << std::endl;
}