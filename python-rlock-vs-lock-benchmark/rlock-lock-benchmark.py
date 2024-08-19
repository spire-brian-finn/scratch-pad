# From chatgpt, massaged by me
import threading
import time

lock = threading.Lock()
rlock = threading.RLock()

def lock_test(lock_obj, iterations):
    for _ in range(iterations):
        with lock_obj:
            time.sleep(0.000001) # sleep for 1 microsec to allow for contention


def benchmark(lock_obj, iterations=1000000, thread_count=10):
    threads = []
    for _ in range(thread_count):
        threads.append(threading.Thread(target=lock_test, args=(lock_obj, iterations)))
    start = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end = time.time()
    return end - start

iterations = 100000
threads = 4
lock_time = benchmark(lock, iterations, threads) 
rlock_time = benchmark(rlock, iterations, threads) 
print(f"Lock time: %s seconds", lock_time)
print(f"RLock time: %s seconds", rlock_time)

"""
### py2, 100k iterations, 4 threads:
Lock time: %s seconds 57.46543478965759
RLock time: %s seconds 70.13392329216003

### py2, 100k iterations, 8 threads:
Lock time: %s seconds 164.1035487651825
RLock time: %s seconds 184.26300239562988

### py3, 100k iterations, 4 threads:
Lock time: %s seconds 59.371614933013916
RLock time: %s seconds 57.764153718948364

### py3, 100k iterations, 8 threads:
Lock time: %s seconds 133.30713415145874
RLock time: %s seconds 134.75239729881287
"""