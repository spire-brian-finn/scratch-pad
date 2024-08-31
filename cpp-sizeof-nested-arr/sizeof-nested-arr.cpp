#include <iostream>

using namespace std;

unsigned char nestedArr[2][3] = {{1,2,3}, {4,5,6}};

int main() {
    cout << "sizeof nullptr: " << sizeof(nullptr) << endl;
    // ^ sizeof nullptr: 8 lolwut
    cout << "sizeof unsigned char nullptr: " << sizeof(static_cast<unsigned char*>(nullptr)) << endl;
    cout << "sizeof nestedArr: " << sizeof(nestedArr) << endl;
    cout << "sizeof nestedArr[0]: " << sizeof(nestedArr[0]) << endl;
}