#include <errno.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

int main() {
    struct timespec precise;
    struct timespec coarse;
    clock_gettime(CLOCK_MONOTONIC, &precise);
    clock_gettime(CLOCK_MONOTONIC_COARSE, &coarse);

    printf("Precise: %ld sec %ld ns\n", precise.tv_sec, precise.tv_nsec);
    printf("Coarse: %ld sec %ld ns\n", coarse.tv_sec, coarse.tv_nsec);

}