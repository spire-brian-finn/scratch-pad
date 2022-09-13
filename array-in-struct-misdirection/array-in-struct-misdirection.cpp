#include <cstdint>
#include <iostream>

typedef struct __attribute__((__packed__)) {
    uint8_t data[100] = {0};
} buffer_t;

int main() {
    buffer_t buffer;
    uint8_t data[100] = {1};
    buffer.data = data;
    // Compiler is upset! It knows the difference between uint8_t array and uint8_t*, and prevents assignment to the former.
}