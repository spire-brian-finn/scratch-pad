#include <iostream>
using namespace std;

class Foo {
    public:
        int var = 0;
        Foo(int dummy __attribute__((unused))) {}
};

class Bar {
    public:
        int var = 0;
        Bar(int dummy __attribute__((unused))) {
            var = 0;
        }
};

Foo f;
Bar b;

int main() {

    void (*f)() = [&]() {
        f(1);
        b(1);
    };

    f.var = 1;
    b.var = 1;

    cout << "f: " << &f << "\tb: " << &b << endl;
    cout << "f: " << f.var << "\tb: " << b.var << endl;

    // Will the default ctor in Foo re-zero f?
    Foo f;
    Bar b;
     
    cout << "f: " << &f << "\tb: " << &b << endl;
    cout << "f: " << f.var << "\tb: " << b.var << endl;
}