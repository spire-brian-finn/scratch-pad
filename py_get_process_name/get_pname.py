import os

cmdline = ""
with open("/proc/%s/cmdline" % os.getpid(), "r") as fh:
    cmdline = fh.read()

parts = cmdline.split("\x00")
if len(parts) > 1:  # e.g. python foo.py quux thud
    pname = parts[1]
elif len(parts == 1):
    pname = parts[0]
else:
    pname = ""

print(" ".join(str(x) for x in cmdline.split("\x00")))