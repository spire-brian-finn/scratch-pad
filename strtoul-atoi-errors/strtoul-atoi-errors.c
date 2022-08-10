#include <stdio.h>
#include <stdlib.h>

int main() {
    char* endptr;
    char* arg = "foobar";
    unsigned long foo = strtoul(arg, &endptr, 10);
    printf("%s yielded %lu\n", arg, foo);

    printf("I suppose I could check endptr == the string. %p %p\n", (void *) arg, (void *) endptr);
}