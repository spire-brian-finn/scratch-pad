import os
import time
import tempfile

def time_os_stat():
    with tempfile.NamedTemporaryFile() as fh:
        fname = fh.name
        start = time.time()
        for _ in range(1000):
           stats = os.stat(fh.name)
           # Time to get file size from stat is
           # negligible; skip it
        end = time.time()
    return end-start

def time_iteration(d):
  start = time.time()
  for k, v in d.items():
    pass
  end = time.time()
  return end-start

def time_duplication(d):
  new_d = {}
  start = time.time()
  for k, v in d.items():
    # let's be fair and say we remove a lot
    if k % 10 == 0:
      new_d[k] = v
  end = time.time()
  return (new_d, end - start)

test = {i:0 for i in range(1000)}

two_iter_time = 2 * time_iteration(test)
new_dict, dup_time = time_duplication(test)
new_dict_iter_time = time_iteration(new_dict)
dup_plus_iter_time = dup_time + new_dict_iter_time
stat_time = time_os_stat()

print(f"Time to stat 1k files: {stat_time}")
print(f"Time to iterate over 1k dict entries twice: {two_iter_time}")
print(f"Time to iterate over 1k entries, copy 100, and iterate over those: {dup_plus_iter_time}")