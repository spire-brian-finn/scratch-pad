import threading
import time

class DaemonThread(threading.Thread):
    def __del__(self):
        print("Look at me I'm a deconstructor")

def spin():
    while True:
        print("Hello from the thread")
        time.sleep(1)

def main():
    beelzebubbles= DaemonThread(target=spin)
    beelzebubbles.daemon = True
    beelzebubbles.start()
    time.sleep(3)
    exit()

if __name__ == "__main__":
    main()