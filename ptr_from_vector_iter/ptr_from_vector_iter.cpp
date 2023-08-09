#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> foo {1,2,3,4,5};
    int* bar = &foo.back();
    cout << bar << endl;
    cout << *bar << endl;
}