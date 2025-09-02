#include <stdio.h>
#include <string.h>

int main() {
    char* sus;
    char* known = "foo";
    printf("known: %p: %s\nsus: %p: %s (%p)\n", known, known, sus, sus, &(sus));
    //int cmp = strncmp(sus, known, strlen(known));
    int cmp = strncmp(sus, known, 100);
    printf("cmp: %d\n", cmp);
    return cmp;
}