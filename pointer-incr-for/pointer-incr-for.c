#include <stdio.h>

int main() {
    int buf[] = {1, 2, 3};
    printf("buf: %zu, int: %zu, start: %p, supposed end: %p\n", sizeof(buf), sizeof(int), buf, buf + sizeof(buf) / sizeof(buf[0]));

    // Pointer math
    for (int* iter = buf; iter < buf + sizeof(buf) / sizeof(buf[0]); ++iter) {
        printf("%p: %d\n", iter, *iter);
    }
}