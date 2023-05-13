#include <stdio.h>

int sum(int* numbers, int nnums) {
    int newnums[nnums];
    int sum = 0;
    for (int i = 0; i < nnums; i++) {
        newnums[i] = numbers[i];
        sum += newnums[i];
    }
    return sum;
}

int main() {
    int numbers[] = {1,2,3,4,5};
    printf("%i\n", sum(numbers, 5));
}