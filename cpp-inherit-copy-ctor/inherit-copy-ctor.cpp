class A {
    public:
      int m_foo = 0;
      virtual void Foo() = 0;
      A() {};
      A(const A&) = delete;
      
      //A operator=(const A&) = delete; <- return type A requires returning an actual A, which isn't possible. But A& is cool
      A& operator=(const A&) = delete;
};

class B: public A {
    public:
        B() {};
        //B(const B& b) {};
        void Foo() {};
};

int main() {
    B b1, b2;
    B b3(b2);
    b1 = b2;
}