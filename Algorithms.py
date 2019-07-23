import math

'''
Binary Search
'''

'''
def binary_search(list,item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = int((low+high)/2)
        guess = list[mid]
        
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid+1
    return None

my_list = [1,2,3,4,5,7,9]

print (binary_search(my_list, 7))
print (binary_search(my_list, -1))

print (round(math.log2(1000000000)))
'''

'''
Selection Sort
'''

#findSmallest
def findSmallest(arr):
    smallest = arr[0] #Stores the smallest value
    smallest_index = 0 #Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

#selection sort
    
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print (selectionSort([5,3,9,1,8]))