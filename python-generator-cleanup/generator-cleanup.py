from contextlib import closing

def test_yield():
    print("Generating")
    try:
        #yield from []
        yield from [1]
    except GeneratorExit:
        print("GeneratorExit")
    finally:
        print("exiting yield")

def test():
    x = test_yield()
    print(f"{x}: {type(x)}")
    #x.close()
    print(f"generated {next(x)}")
    #del x
    print("deleted generator")

test()
print("done")
