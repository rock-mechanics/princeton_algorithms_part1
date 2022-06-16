import random

# Merging with smaller auxiliary array. 
# Suppose that the subarray a[0] to a[n−1] is sorted 
# and the subarray a[n] to a[2∗n−1] is sorted. 
# How can you merge the two subarrays so that 
# a[0] to a[2∗n−1] is sorted using an auxiliary array 
# of length n (instead of 2n)?

def merge(arr, aux, low, mid, hig) : 
    left = low
    right = mid
    # we do this step by step, each time we process len(aux)
    for i in range(low, hig, len(aux)) : 
        # find the ith oredered segment
        # fill it in the aux array
        upper_bound = i + len(aux)
        if upper_bound > len(arr) : upper_bound = len(arr)
        # fill in the aux arr
        for j in range(i, upper_bound) : 
            if (left >= mid) : 
                aux[j % len(aux)] = arr[right]
                right += 1
            elif (right >= hig) : 
                aux[j % len(aux)] = arr[left]
                left += 1
            elif (arr[left] < arr[right]) : 
                aux[j % len(aux)] = arr[left]
                left += 1
            else : 
                aux[j % len(aux)] = arr[right]
                right += 1
        # now aux contains the sorted len(aux) elements

        # move the arr
        # we move the remaining left segment to right
        dist = right - mid
        # we need to exclude right pointer -> right - 1
        # we need to include left pointer -> left + dist - 1
        for j in range(right - 1, left + dist - 1, -1) : 
            arr[j] = arr[j - dist]
        
        # we update the pointer position
        left = left + dist
        mid = right

        # we copy the aux to arr
        for k in range(len(aux)) : 
            if i + k < len(arr) : 
                arr[i + k] = aux[k]

# testing engine
arr = [i for i in range(5)]
for i in range(5) : arr.append(i) 
print(f'arr initiaized : {arr}')
aux = [None for i in range(3)]
print(f'aux initialize : {aux}')
merge(arr, aux, 0, 5, len(arr))
print('after sorting')
print(arr)