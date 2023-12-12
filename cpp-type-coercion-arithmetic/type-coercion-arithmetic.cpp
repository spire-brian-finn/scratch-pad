#include <cstdint>
#include <iostream>

int main() {
    int64_t signedInt = -10;
    uint64_t unsignedInt = 1;
    int64_t signedIntPositive = 10;
    std::cout << unsignedInt - signedInt << std::endl;
    std::cout << unsignedInt + signedInt << std::endl;
    std::cout << unsignedInt + static_cast<uint64_t>(signedInt) << std::endl;
    std::cout << unsignedInt - signedIntPositive << std::endl;
    std::cout << unsignedInt + signedIntPositive << std::endl;
    double doubleVal = 2.5;
    int divisor = 2;
    auto quotient = doubleVal / divisor;
    std::cout << quotient << std::endl;
}