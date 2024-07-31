import optparse

if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("-f", "--foo")
    opts, args = parser.parse_args()
    print("%s %s" % (opts, args))