# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "attrs==19.3.0",
#     "rich",
# ]
# ///
import copy
import attr
from rich.pretty import pprint


@attr.s
class Foo(object):
    a = attr.ib()
    b = attr.ib()


def main():
    f = Foo(1, 2)
    pprint(f)
    pprint(dir(f))

    f2 = copy.deepcopy(f)
    pprint(f2)
    pprint(dir(f2))

    print(f"same obj: {id(f) == id(f2)}")
    print(f"same cmp: {f == f2}")


if __name__ == "__main__":
    main()
