#include <iostream>
#include <vector>

int sum(std::vector<int> numbers) {
    int operands[numbers.size()];
    for (int i = 0; i < numbers.size(); i++) {
        operands[i] = numbers[i];
    }

    int sum = 0;
    for (int i = 0; i < numbers.size(); i++) {
        sum += operands[i];
    }
    return sum;
}

int main() {
    std::vector<int> numbers {1, 2, 3, 4, 5};
    std::cout << sum(numbers) << std::endl;
}

/*
note from Jeff:
oof.   variable length arrays (VLAs) were included in C99 but not in C++ (as of at least c++14, not clear on more recent but it seems still not) and the topic seems to have been hotly debated for a while.  However, gcc and clang do support them, but there's also a warning that can be enabled -Werror=vla
*/