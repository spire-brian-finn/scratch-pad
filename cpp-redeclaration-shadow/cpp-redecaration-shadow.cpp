#include <iostream>

using namespace std;

int main() {
    unsigned int foo = 1;
    unsigned int bar = 1;
    //if (true) {
    {
        unsigned int foo = 2;
        bar = 2;
        cout << "Inside \"if\", foo: " << foo << " bar: " << bar << endl;
    }
    cout << "After \"if\", foo: " << foo << " bar: " << bar << endl;
    return 0;
}
