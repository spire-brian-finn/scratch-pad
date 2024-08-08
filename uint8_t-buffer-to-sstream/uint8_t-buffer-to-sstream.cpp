#include <iomanip>
#include <iostream>
#include <sstream>

#define SIZE 40

int main() {
    uint8_t buf[SIZE];
    for (uint8_t i = 0; i < SIZE; i++) {
        buf[i] = i % 16;
    }

    std::stringstream s;
    s << "start ";
    s << std::hex << std::uppercase << std::setfill('0');
    for (int i = 0; i < SIZE; i++) {
        //s << std::hex << std::uppercase << std::setw(2) << std::setfill('0') << static_cast<unsigned short>(buf[i]) << " ";
        s << std::setw(2) << static_cast<unsigned short>(buf[i]) << " ";
        //s << buf[i];
    }
    s << " end";
    printf(s.str().c_str());
    //std::cout << s.str() << std::flush;

}