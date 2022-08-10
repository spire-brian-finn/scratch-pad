#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char* endptr;
    char* arg = "foobar";
    unsigned long foo = strtoul(arg, &endptr, 10);
    printf("Arg: %s foo: %lu argptr: %p endptr: %p\n", arg, foo, (void *)arg, (void *) endptr);
    printf("Errno %d: %s\n", errno, strerror(errno));

    char* correct_arg = "11";
    foo = strtoul(correct_arg, &endptr, 10);
    printf("Arg: %s foo: %lu argptr: %p endptr: %p\n", correct_arg, foo, (void *)correct_arg, (void *) endptr);
    printf("Errno %d: %s\n", errno, strerror(errno));
    printf("argptr + strlen: %p value at argptr + strlen: %d endptr: %p\n",
           (void *) correct_arg + strlen(correct_arg), correct_arg[strlen(correct_arg)], (void *) endptr);
    
    char* extra_stuff_arg = "11 and some bonus stuff";
    foo = strtoul(arg, &endptr, 10);
    printf("Arg: %s foo: %lu argptr: %p endptr: %p\n", extra_stuff_arg, foo, (void *)extra_stuff_arg, (void *) endptr);
    printf("Errno %d: %s\n", errno, strerror(errno));
    printf("argptr + strlen: %p value at argptr + strlen: %d endptr: %p\n",
           (void *) extra_stuff_arg + strlen(correct_arg), extra_stuff_arg[strlen(extra_stuff_arg)], (void *) endptr);
}