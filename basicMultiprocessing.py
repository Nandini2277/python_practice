# (multiprocessing code needs the `if __name__ == "__main__":` guard on Windows/macOS).

# 16a. BASIC MULTIPROCESSING
import os
import time
from multiprocessing import Process


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()

    # create processes
    for i in range(num_processes):
        p = Process(target=square_numbers)
        processes.append(p)

    # start
    for p in processes:
        p.start()

    # join
    for p in processes:
        p.join()

    print("end main")