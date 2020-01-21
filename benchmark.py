from random import randrange
from selection_sort import selection_sort
from bubble_sort import bubble_sort
from timeit import time

# Creo la lista
# Lista di partenza da ordinare
mylist = [randrange(1000) for _ in range(10000)]

# Calcolo i tempi del selection sort....
selection_sort_time = selection_sort(mylist.copy())

# Calcolo i tempi del bubble sort....
bubble_sort_time = bubble_sort(mylist.copy())

# Calcolo i tempi del sort di default di python....
newlist = mylist.copy()

start_time = time.time()
newlist.sort()
stop_time = time.time()

default_sort_time = stop_time-start_time

# Salvo i risultati su file
result_file = open("results.csv","a")
result_file.write(f"{len(mylist)},{selection_sort_time},{bubble_sort_time},{default_sort_time}\n")
result_file.close()