from threading import Thread
import os
import time

def square_number():
    for i in range(10):
        i*i
        time.sleep(0.1)

threads=[]
num_threads=os.cpu_count()

for i in range(num_threads):
    t=Thread(target=square_number)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print('end main')