#include <stdio.h>
#include <sys/types.h>

#define HL 13
#define TL 2
#define TLL 4

int main(int ac, char**av) {
    ssize_t ab = 0; // as opposed to int64_t
    size_t ql = 0;

    for (ql=0; ql<30; ql++) {
        ab = 4000;
        ab -= ql - HL - TL - TLL;
        printf("ab: %zd\n", ab);
    }
    return 0;
}