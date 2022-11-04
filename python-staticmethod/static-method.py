class Foo:
    def method(self):
        print("Hello from method")
        self.staticky()
    
    @staticmethod
    def staticky():
        print("stasis")

Foo.staticky()
Foo().staticky()
Foo().method()
