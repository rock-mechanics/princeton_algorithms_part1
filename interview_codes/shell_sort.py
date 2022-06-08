from operator import is_
import random

class sort_machine:
    def __init__(self) : 
        self.comp_count = 0
        self.swap_count = 0
    def clear_count(self) : 
        self.comp_count = 0
        self.swap_count = 0
    def insertion_sort(self, arr) : 
        if (len(arr) == 1) : 
            return
        for i in range(1, len(arr)) : 
            for j in range(i , 0, -1) : 
                self.comp_count += 1
                if (arr[j] < arr[j - 1]) : 
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    self.swap_count += 1
                else : 
                    break
    
    def shell_sort(self, arr) : 
        # shell sort use h sort from large number to 1
        # we need to make sure, h will fall back to 1, not 0.
        # initialize h
        h = 1
        # there is log3(n) number of h
        while (h < len(arr) / 3) : 
            h = h * 3 + 1
        
        # best case : if arr is already sorted. we follow insertion sort from h - len(arr)
        # we just need to confirm ~N times
        # in total we need to compare ~log3(N)*N times and make no swap at all

        while (h >= 1) : 
            # we insertion sort the arr in gap of h
            for i in range(h, len(arr)) : 
                for j in range(i, 0, -h) : 
                    self.comp_count += 1
                    if (arr[j] < arr[j-h]) : 
                        self.swap_count += 1
                        arr[j], arr[j-h] = arr[j-h], arr[j]
                    else : 
                        break
            h = h // 3

# check arr if it is sorted
def is_sorted(arr) : 
    for i in range(1, len(arr)) : 
        if (arr[i] < arr[i - 1]) : 
            return False
    return True

# test 
arr = [random.randint(0,100) for i in range(100)]
arr_copy = arr[:]

print(is_sorted(arr_copy))
print(is_sorted(arr))

s = sort_machine()
s.clear_count()
s.insertion_sort(arr)
print(f"insertion  : {s.comp_count} compares and {s.swap_count} swaps")
print(f"insertion  : {is_sorted(arr)}")
s.clear_count()
s.shell_sort(arr_copy)
print(f"shell sort : {s.comp_count} compares and {s.swap_count} swaps")
print(f"shell sort : {is_sorted(arr_copy)}")
