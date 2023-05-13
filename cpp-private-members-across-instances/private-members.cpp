#include <iostream>

class Obj {
    private:
    const int foo;

    public:
    Obj(int foo);
    int AddFoo(const Obj& other);
    static int Add(const Obj& a, const Obj& b);
};

Obj::Obj(int foo): foo(foo) {};
int Obj::AddFoo(const Obj& other) {
    return foo + other.foo;
}
int Obj::Add(const Obj& a, const Obj& b) {
    return a.foo + b.foo;
}

int main() {
    Obj a(1);
    Obj b(2);
    std::cout << a.AddFoo(b) << std::endl;
    std::cout << Obj::Add(a, b) << std::endl;
}