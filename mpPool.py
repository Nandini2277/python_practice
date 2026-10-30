# 18d. MULTIPROCESSING: Pool
from multiprocessing import Pool

def cube(number):
    return number * number * number

if __name__ == "__main__":
    numbers = range(10)

    p = Pool()
    # by default uses as many processes as CPU cores; splits data into chunks
    result = p.map(cube, numbers)

    p.apply(cube, args=(numbers[0],))      # run a single call

    p.close()
    p.join()
    print(result)