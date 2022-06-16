# Counting inversions. 
# An inversion in an array a[] is a pair of entries a[i]and a[j] such that i < j 
# but a[i] > a[j]. Given an array, 
# design a linearithmic algorithm to count the number of inversions.

def count_inversions(arr, aux, low, hig) : 
    # one elements / no elements. no inversions
    if (hig - low <= 1) : return 0
    # we we do merge sort, we eliminate the inversions
    mid = (low + hig) // 2
    # count the inversions and sort the sub array
    count_first = count_inversions(arr, aux, low, mid)
    count_second = count_inversions(arr, aux, mid, hig)
    # since sub arr is sorted, if we count again, we only count the inversions
    # between two segments
    return count_first + count_second + merge_count(arr, aux, low, mid, hig)

def merge_count(arr, aux, low, mid, hig) : 
    # assume low - mid is sorted
    # assume mid - hig is sorted
    # count the number of inversions for two sorted arr
    # as a side effect, we sort the array from low - hig
    # so we eliminates the inversions from low - hig, so we don't count twice

    count = 0
    # copy arr to aux 
    for i in range(low, hig) : 
        aux[i] = arr[i]
    # set up the pointer to go through the left portion and right portion
    left = low
    right = mid
    for i in range(low, hig) : 
        if (left >= mid) : 
            arr[i] = aux[right]
            right += 1
        elif (right >= hig) : 
            # we will only count when right piece is used
            arr[i] = aux[left]
            left += 1
        elif (aux[left] <= aux[right]) : 
            arr[i] = aux[left]
            left += 1
        else : 
            # we put a right piece
            arr[i] = aux[right]
            right += 1
            # if we put a right piece, the number of inversion created is 
            # the number of left pieces used.
            count += mid - left
    return count

arr = [ i for i in range(5, 0, -1)]
print(arr)
aux = arr[:]
count = count_inversions(arr, aux, 0, len(arr))
print(arr)
print(count)