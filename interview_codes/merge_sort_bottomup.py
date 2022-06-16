import random

class sort_machine : 
    def __init__(self) : 
        pass
    def merge_sort_bu(self, arr, aux) : 
        # we double the size each time
        sz = 2
        # in the end, the sz will overflow the arr
        # so the whole arr will be sorted
        while (sz < 2 * len(arr)) : 
            # we loop the arr for each size
            for i in range(0, len(arr), sz) : 
                # upper bound
                upper_bound = i + sz
                if (upper_bound > len(arr)) : upper_bound = len(arr)
                # lower bound
                lower_bound = i
                # the size is doubled in the previous step
                # we half the size and get the original mid point
                midle_bound = i + sz // 2
                # we merge the two sorted sub array
                self.merge(arr, aux, lower_bound, midle_bound, upper_bound)
            # we double the size
            sz *= 2
    
    # normal merge for merge sort
    def merge(self, arr, aux, low, mid, hig) : 
        # copy arr
        for i in range(low, hig): 
            aux[i] = arr[i]
        # merge
        left = low
        right = mid
        for i in range(low, hig) : 
            if (left >= mid):
                arr[i] = aux[right]
                right += 1
            elif (right >= hig) : 
                arr[i] = aux[left]
                left += 1
            elif aux[left] < aux[right] : 
                arr[i] = aux[left]
                left += 1
            else : 
                arr[i] = aux[right]
                right += 1

# test driver
arr = [random.randint(1,100) for i in range(10)]
aux = arr[:]
print(arr)
s = sort_machine()
s.merge_sort_bu(arr, aux)
print(arr)