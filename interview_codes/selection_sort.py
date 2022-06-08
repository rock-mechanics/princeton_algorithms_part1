import random

# for sorter array, you pick a pointer. there will be two invariants
# invariant 1 : all elements on the left side of the pointer less than the pointer
# invariant 2 : all elements on the right side of the pointer is bigger than the pointer

# for i = 0. no element on the left side. invariant 1 preserve
# for i = 0. invariant 2 broken, we find the smallest. and swap with the pointer.
# after that invariant 2 preserve
# we move the pointer to next slot
# invariant 2 broken again. we fix it using the same method again.
# when we reach len(arr), both invariants preserve

class selection_sort : 
    def __init__(self) : 
        self.swap_count = 0
        self.comp_count = 0
    def sel_sort(self, arr) : 
        for i in range(len(arr)) : 
            for j in range(i + 1, len(arr)) : 
                self.comp_count += 1
                if arr[j] < arr[i] : 
                    arr[j], arr[i] = arr[i], arr[j]
                    self.swap_count += 1 

arr = [random.randint(0,100) for i in range(10)]
print(arr)
s = selection_sort()
s.sel_sort(arr)
print(arr)
print(f"{s.comp_count} compares and {s.swap_count} swaps")