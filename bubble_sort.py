from timeit import time

def bubble_sort(list):
    start_time = time.time()

    for index in range(len(list)):
        swapped = False
        for jdex in range(index, len(list)):
            if (list[index] > list[jdex]):
                list[index], list[jdex] = list[jdex], list[index]
                swapped = True
        if not swapped:
            break

    stop_time = time.time()
    return stop_time-start_time