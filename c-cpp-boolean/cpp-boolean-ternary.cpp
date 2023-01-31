#include <iostream>

using namespace std;

int main() {
    int mod0 = 3 % 3 ? 1 : 0;
    int mod1 = 3 % 2 ? 1 : 0;
    int mod2 = 5 % 3 ? 1 : 0;
    cout << "mod returns 0: " << mod0 << endl;
    cout << "mod returns 1: " << mod1 << endl;
    cout << "mod returns 2: " << mod2 << endl;
}