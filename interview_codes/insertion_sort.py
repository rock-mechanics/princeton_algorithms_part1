import random
# for any sorted array, if you pick one pointer
# there exists one invariant
# invariant 1 : the array on the left (including the pointer) is sorted

# insertion sort swaps and compares
# the swaps equals to the number of inversions
# the compares equals to the number of inversions + N - 1
# we have to make the compare even the arr on left including i is perfectly sorted.

class sort_machine:
    def __init__(self) : 
        self.comp_count = 0
        self.swap_count = 0
    def insertion_sort(self, arr) : 
        # keep the invariant the all elemnts on the left side of i is sorted
        # we start from index 1 as there is no need to sort one element arr
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

arr = [random.randint(0,100) for i in range(10)]
arr = [ i for i in range(10, 0, -1)]
print(arr)
s = sort_machine()
s.insertion_sort(arr)
print(arr)
print(f"{s.comp_count} compares and {s.swap_count} swaps")
