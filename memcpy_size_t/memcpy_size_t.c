#include <endian.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

int main() {
    uint8_t buffer[2];
    size_t shorty = 223;
    uint8_t *shorty_ptr = (uint8_t*) &shorty;
    shorty_ptr += sizeof(size_t) - 1;
    memcpy(buffer, shorty_ptr, 1);
    printf("copied in the value %hhu\n", buffer[0]);

    *buffer = shorty;
    printf("assignment produced value %hhu\n", buffer[0]);
}