import threading

def test_local_singletonicity():
    setattr(threading.local(), "wie_gehts", "mir geht's gut!")
    print(getattr(threading.local(), "wie_gehts", "mir geht's nicht so gut"))

if __name__ == "__main__":
    t = threading.Thread(target=test_local_singletonicity)
    t.start()
    t.join()