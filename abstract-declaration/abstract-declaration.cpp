#include <iostream>

class Base {
    public:
        //virtual void foo() = 0;
        virtual void foo() {
            std::cout << "oh no" << std::endl;
        };

        virtual ~Base() {
            std::cout << "goodbye base" << std::endl;
        }

        Base(const Base& other) {
            std::cout << "copying a Base" << std::endl;
        }
};

class DerivativeOne : public Base {
    public:
        virtual void foo() {
            std::cout << "hello" << std::endl;
        }

        ~DerivativeOne() {
            std::cout << "d1structor" << std::endl;
        }
};

class DerivativeTwo : public Base {
    public:
        virtual void foo() {
            std::cout << "world" << std::endl;
        }

        ~DerivativeTwo() {
            std::cout << "d2structor" << std::endl;
        }
};

int main() {
    Base real;
    Base* whatCouldItBe = &real;
    //Base& whatCouldItBe = real;
    for (int i = 0; i < 2; ++i) {
        if (i % 2 == 0) {
            DerivativeOne d1;
            whatCouldItBe = &d1;
            whatCouldItBe->foo();
        } else {
            DerivativeTwo d2;
            whatCouldItBe = &d2;
            whatCouldItBe->foo();
        }
        whatCouldItBe->foo();
    }
}