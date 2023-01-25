import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--spire-id', default=None, help="spire id for metadata")
    args, other_args = parser.parse_known_args()
    print("args: {}".format(args))
    print("other args:{}".format(other_args))