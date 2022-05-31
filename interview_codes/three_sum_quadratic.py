import random;
import time;

# Given an array of integers 
# find all triplets in the array that sum up to a given target value. 
# we need to finish it in ~N*N time

# correct answer from internet
def quad_search_three_sums(arr) : 
    bubble_sort(arr)
    three_sums = []
    for number in arr :
        reciprocal = - number
        two_sums = find_two_sum(arr, reciprocal) 
        for num1, num2 in two_sums : 
            three_sums.append((reciprocal, num1, num2))
    return three_sums

def find_two_sum(arr, number) : 
    # give the arr is sorted and unique
    starting = 0
    ending = len(arr) - 1
    while starting < ending : 
        if (arr[starting] + arr[ending] > number) : 
            # we need to decrease the sum, the only way is to decrease the large number
            ending -= 1
        elif (arr[starting] + arr[ending] < number) :  
            # increase the sum
            starting += 1
        else : 
            return [(arr[starting], arr[ending])]
    return [] 

def bubble_sort(arr) : 
    for i in range(0, len(arr) - 1) : 
        for j in range(0, len(arr) - 1 - i) : 
            if arr[j] > arr[j + 1] : 
                arr[j] , arr[j + 1] = arr[j + 1] , arr[j]

arr = [i for i in range(-3,3)]
random.shuffle(arr)
print(arr)
# internet method
print(quad_search_three_sums(arr))