import random
import time
import math

def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 # Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
        
def shellSort(arr): 
  
    # Start with a big gap, then reduce the gap 
    n = len(arr) 
    gap = n/2
    gap = int(gap)
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array 
    # is gap sorted 
    while gap > 0: 
  
        for i in range(gap,n): 
  
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = arr[i] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
  
            # put temp (the original a[i]) in its correct location 
            arr[j] = temp 
        gap /= 2
        gap = int(gap)

def truncate(number, decimals=0):
    """
    Returns a value truncated to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor


totalb = 0
averageb = 0
totalm = 0
averagem = 0
totalq = 0
averageq = 0
totals = 0
averages = 0

low = 0
high = 998

a_list = list(range(1, 1000))
    
#random.shuffle(a_list)
    
a_listcopy = a_list.copy()

# start = time.perf_counter_ns()
# bubbleSort(a_list)
# stop = time.perf_counter_ns()
# #print(a_list)
# duration = (stop - start)
# print("Bubble sort completed " + str(duration) + " seconds")
# totalb = totalb + duration

# a_list = a_listcopy.copy()
# start = time.perf_counter_ns()
# mergeSort(a_list)
# stop = time.perf_counter_ns()
# #print(a_list)
# duration = (stop - start)
# print("Merge sort completed " + str(duration) + " seconds")
# totalm = totalm + duration

a_list = a_listcopy.copy()
start = time.perf_counter_ns()
quickSort(a_list, low, high)
stop = time.perf_counter_ns()
#print(a_list)
duration = truncate(((stop - start)* 10**-9), 7)
print("Quick sort completed " + str(duration) + " seconds")
totalq = totalq + duration

# a_list = a_listcopy.copy()
# start = time.perf_counter_ns()
# shellSort(a_list)
# stop = time.perf_counter_ns()
# #print(a_list)
# duration = (stop - start)
# print("Shell sort completed " + str(duration) + " seconds")
# totals = totals + duration


# for x in range(0, 1000):
#     low = 0
#     high = 998
    
#     a_list = list(range(1, 1000))
    
#     random.shuffle(a_list)
    
#     a_listcopy = a_list.copy()
    
#     start = time.perf_counter_ns()
#     bubbleSort(a_list)
#     stop = time.perf_counter_ns()
#     #print(a_list)
#     duration = (stop - start)
#     #print("Bubble sort completed " + str(duration) + " seconds")
#     totalb = totalb + duration
    
#     a_list = a_listcopy.copy()
#     start = time.perf_counter_ns()
#     mergeSort(a_list)
#     stop = time.perf_counter_ns()
#     #print(a_list)
#     duration = (stop - start)
#     #print("Merge sort completed " + str(duration) + " seconds")
#     totalm = totalm + duration
    
#     a_list = a_listcopy.copy()
#     start = time.perf_counter_ns()
#     quickSort(a_list, low, high)
#     stop = time.perf_counter_ns()
#     #print(a_list)
#     duration = (stop - start)
#     #print("Quick sort completed " + str(duration) + " seconds")
#     totalq = totalq + duration
    
#     a_list = a_listcopy.copy()
#     start = time.perf_counter_ns()
#     shellSort(a_list)
#     stop = time.perf_counter_ns()
#     #print(a_list)
#     duration = (stop - start)
#     #print("Shell sort completed " + str(duration) + " seconds")
#     totals = totals + duration
    
    
# averageb = truncate(((totalb/1000)* 10**-9), 7)
# print(averageb)
# averagem = truncate(((totalm/1000)* 10**-9), 7)
# print(averagem)
# averageq = truncate(((totalq/1000)* 10**-9), 7)
# print(averageq)
# averages = truncate(((totals/1000)* 10**-9), 7)
# print(averages)
