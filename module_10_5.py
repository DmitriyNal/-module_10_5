import os
import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            lines = file.readlines()
            if not lines:
                break
            for line in lines:
                all_data.append(line)



if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start = time.time()
    for filename in filenames:
        read_info(filename)
    end = time.time()
    print(end - start, '(линейный)')

    start = time.time()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    end = time.time()
    print(end - start, '(многопроцессный)')


