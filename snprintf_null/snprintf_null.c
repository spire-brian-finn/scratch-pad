#include <stdio.h>

int main() {
    int i = snprintf(NULL, 0, "fmt %d", 1);
    printf("returned: %d\n", i);
}