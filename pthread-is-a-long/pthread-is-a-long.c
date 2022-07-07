#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

void* do_nothing() {}

int main() {
    pthread_t* foo = calloc(1, sizeof(pthread_t));
    // Trusting that calloc works.

    printf("Thread is initially %lu\n", *foo);
    pthread_create(foo, NULL, do_nothing, NULL);
    printf("Thread is %lu after pthread_create\n", *foo);
}