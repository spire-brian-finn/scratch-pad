import timeit

init="""
import struct

msg="hello world, I am very well how are you"*4
# assuming pmt.cdr is a vector of bytes
msgvec=list(bytearray(msg))
arr=bytearray(msg)
print(msgvec)
"""

stmt1="""
length = len(msgvec)
fmt_str = '>I%ss' % (length,)
struct.pack(fmt_str, length, ''.join(chr(i) for i in msgvec))
"""

stmt2="""
length = len(msgvec)
fmt_str = '>I%db' % (length,)
struct.pack(fmt_str, *([length] + msgvec))
"""

stmt3="""
length = len(msgvec)
fmt_str = '>I'
struct.pack(fmt_str, length) + str(bytearray(msgvec))
"""

stmt4="""
length = len(arr)
fmt_str = '>I%ss' % (length,)
struct.pack(fmt_str, length, ''.join(chr(i) for i in arr))
"""

S1 = timeit.Timer(setup=init, stmt=stmt1)
S2 = timeit.Timer(setup=init, stmt=stmt2)
S3 = timeit.Timer(setup=init, stmt=stmt3)
S4 = timeit.Timer(setup=init, stmt=stmt4)

n=10000
print("S1: {}".format(S1.timeit(number=n)))
print("S2: {}".format(S2.timeit(number=n)))
print("S3: {}".format(S3.timeit(number=n)))
print("S4: {}".format(S4.timeit(number=n)))