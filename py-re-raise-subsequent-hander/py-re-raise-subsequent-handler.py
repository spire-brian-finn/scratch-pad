if __name__ == "__main__":
    try:
        raise Exception("e")
    except Exception as e:
        print("Exception handler for %s" % e)
        raise
    except BaseException as e:
        print("BaseException handler for %s" % e)