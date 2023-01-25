import attr

@attr.s
class Foo(object):
    a = attr.ib()
    b = attr.ib()

def main():
    f = Foo(1,2)
    print(f)

if __name__ == "__main__":
    main()