import attr

@attr.s
class Foo(object):
    mandatory = attr.ib(type=str)
    optional = attr.ib(type=int, default=0)
    fact = attr.ib(factory=list)

if __name__ == "__main__":
    f = Foo(mandatory="hey")
    print(f)