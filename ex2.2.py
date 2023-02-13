# import sys
# import json
# import matplotlib.pyplot as plt

# sys.setrecursionlimit(20000)

# def func1(arr, low, high):
#     if low < high:
#         pi = func2(arr, low, high)
#         func1(arr, low, pi-1)
#         func1(arr, pi + 1, high)

# def func2(array, start, end):
#     p = array[start]
#     low = start + 1
#     high = end
#     while True:
#         while low <= high and array[high] >= p:
#             high = high - 1
#         while low <= high and array[low] <= p:
#             low = low + 1
#         if low <= high:
#             array[low], array[high] = array[high], array[low]
#         else:
#             break
#     array[start], array[high] = array[high], array[start]
#     return high

# # Read the JSON file
# with open('data.json', 'r') as f:
#     data = json.load(f)

# # Convert the JSON data into a Python list
# arr = data['array']

# # Call the func1 function to sort the list
# func1(arr, 0, len(arr) - 1)

# # Plot the sorted list
# plt.plot(arr)
# plt.show()

import sys
sys.setrecursionlimit(20000)
import matplotlib.pyplot as plt
import json
import time


def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def test_quicksort(filename):

    with open(filename, 'r') as f:
        data = json.load(f)
    timings = []
    for arr in data:
        start_time = time.time()
        func1(arr, 0, len(arr) - 1)
        end_time = time.time()
        timings.append(end_time - start_time)
    
    plt.plot(timings)
    plt.xlabel('Array number')
    plt.ylabel('Time (seconds)')
    plt.title('QuickSort Timing Results')
    plt.show()

if __name__ == '__main__':
    test_quicksort('ex2.json')
