import os
import signal
import thread

og_signal_handler = signal.getsignal(signal.SIGINT)
print("OG signal handler: %s", og_signal_handler)

def new_signal_handler(signum, frame):
    print("new signal handler invoked for signal %d" % signum)
    # os.kill(os.getpid(), signum) # NOPE this will sink us into a forever loop
    #raise KeyboardInterrupt # This works but isn't quite right for anything but sigint
    og_signal_handler(signum, frame) # Works for all signals but relies on a global reference to the original handler

signal.signal(signal.SIGINT, new_signal_handler)

try:
    #os.kill(os.getpid(), signal.SIGINT) # invokes signal handler
    #raise KeyboardInterrupt # does _not_ invoke signal handler; goes straight to exception handler
    thread.interrupt_main() # invokes signal handler
except KeyboardInterrupt as e:
    print("exception handler invoked")

print("sigterm handler: %s" % signal.getsignal(signal.SIGTERM))
try:
    os.kill(os.getpid(), signal.SIGTERM)
except BaseException as e:
    print("sigterm gave us %s" % e)