try:
    raise Exception()
except Exception as e:
    print("took exception")
else:
    print("no exceptions")
finally:
    print("done")

# note to future me: the order try-except-else-finally appears to be fixed