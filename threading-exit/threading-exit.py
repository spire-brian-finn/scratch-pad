import thread
import threading
import time

#exit_flag = False

def thread_main():
    #blocks forever when main is interrupted
    #while True:
    #    time.sleep(1)
    print('thread sleeping for 10s')
    time.sleep(10)
    print('thread exiting; should see main exit now')

def main_loop():
    print('creating thread')
    t = threading.Thread(target=thread_main)
    t.start()
    print('thread is running; starting main loop')
    time.sleep(5)
    thread.interrupt_main()
    print('exiting main loop')

if __name__ == '__main__':
    main_loop()