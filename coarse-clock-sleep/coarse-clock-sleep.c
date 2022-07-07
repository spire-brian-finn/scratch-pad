#include <errno.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

int main() {
    struct timespec t;
    t.tv_sec = 1;
    t.tv_nsec = 1;
    int ret = clock_nanosleep(CLOCK_MONOTONIC_COARSE, 0, &t, NULL);
    printf("Sleeping returned %d\n", ret);
    if (ret != 0) {
        printf("EFAULT: %d\n", ret == EFAULT);
        printf("EINTR: %d\n", ret == EINTR);
        printf("EINVAL: %d\n", ret == EINVAL);
        printf("ENOTSUP: %d\n", ret == ENOTSUP);
        printf("The cow says %s\n", strerror(ret));
    }
    return 0;
}