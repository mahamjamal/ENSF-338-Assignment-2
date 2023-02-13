import sys
sys.setrecursionlimit(20000)
import matplotlib.pyplot as plt
import json
import random
import time

def quick_sort(arr, low, high):
    while low < high:
        pi = partition(arr, low, high)
        if pi - low < high - pi:
            quick_sort(arr, low, pi-1)
            low = pi + 1
        else:
            quick_sort(arr, pi + 1, high)
            high = pi - 1

def insertion_sort(arr, low, high):
    for i in range(low+1, high+1):
        key_item = arr[i]
        j = i - 1
        while j >= low and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

def partition(array, start, end):
    if end - start <= 10:
        insertion_sort(array, start, end)
        return end
    pivot = random.randint(start, end)
    array[start], array[pivot] = array[pivot], array[start]
    p = array[start]
    i = start + 1
    j = end
    while True:
        while i <= j and array[i] <= p:
            i = i + 1
        while i <= j and array[j] >= p:
            j = j - 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            break
    array[start], array[j] = array[j], array[start]
    return j

def test_quicksort(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    timings = []
    for arr in data:
        start_time = time.time()
        quick_sort(arr, 0, len(arr) - 1)
        end_time = time.time()
        timings.append(end_time - start_time)
    
    plt.plot(timings)
    plt.xlabel('Array number')
    plt.ylabel('Time (seconds)')
    plt.title('QuickSort Timing Results')
    plt.show()

if __name__ == '__main__':
    test_quicksort('ex2.json')