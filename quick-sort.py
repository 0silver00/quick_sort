import timeit
import os
import psutil
import pandas
import csv

process = psutil.Process(os.getpid())
mem_before = process.memory_info().rss / 1024 / 1024
start_time = timeit.default_timer()

def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = list[len(list)//2]
    less_arr, equal_arr, big_arr = [],[],[]

    for i in list:
        if i < pivot :
            less_arr.append(i)
        elif i > pivot :
            big_arr.append(i)
        else:
            equal_arr.append(i)
    return quick_sort(less_arr) + equal_arr + quick_sort(big_arr)

datalist = []

with open('output.csv', 'r') as raw:
    reader = csv.reader(raw)
    for lines in reader:
        datalist.append(lines)

print(quick_sort(list(map(int,datalist[0]))))

end_time = timeit.default_timer()
mem_after = process.memory_info().rss / 1024 / 1024

print("time: %0.3lf" % (end_time - start_time))
print("size: %0.3lf" % (mem_after - mem_before))
