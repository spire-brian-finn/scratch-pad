#include <iostream>
#include <string>

class A {
    private:
        std::string m_name;

    public:
        A();
        void PrintName();
};

A::A() : m_name(__func__) {
}
void A::PrintName() {
    std::cout << m_name << std::endl;
}

class B: public A {};

int main() {
    B b;
    b.PrintName();
}