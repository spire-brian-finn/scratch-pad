#include <stdio.h>

//#define NEGATIVE_MACRO -1
//#define MACRO_FOR_VAR x
#define NEGATIVE_MACRO_FOR_VAR -x

/*
typedef enum {
    A_CONSTANT = -1
} constant_t;
*/

int main() {
    //printf("-NEGATIVE_MACRO: %d\n", -NEGATIVE_MACRO);
    //printf("-A_CONSTANT: %d\n", -A_CONSTANT);
    int x = -1;
    printf("-NEGATIVE_MACRO_FOR_VAR: %d\n", -NEGATIVE_MACRO_FOR_VAR);
    printf("Explicit `- -x`: %d\n", - -x);
    //printf("Resultant var: %d\n", x);
}