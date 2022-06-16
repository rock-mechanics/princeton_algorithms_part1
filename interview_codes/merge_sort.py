import random

class sort_machine : 
    def __init__(self, arr) : 
        # initalize the result
        self.com_count = 0
        self.arr_count = 0
        # the array to be sorted
        self.arr = arr
        # a helper arr to record the sub-sorted array before we modify it
        self.helper = [None for i in range(len(arr))]
    
    def is_sorted(self, arr, low, hig) : 
        if (hig - low <= 1) : 
            return True
        for i in range(low + 1, hig) : 
            if (arr[i] < arr[i - 1]) : 
                return False
        return True

    def merge(self, low_index, mid_index, hig_index) : 
        # assume arr[low_index : mid_index] is sorted
        # assume arr[mid_index : hig_index] is sorted
        assert(self.is_sorted(self.arr, low_index, mid_index))
        assert(self.is_sorted(self.arr, mid_index, hig_index))

        # we keep a copy of the arr first
        # so we have these two sub sorted arr at hand
        for i in range(low_index, hig_index) : 
            self.helper[i] = self.arr[i]
        
        # then we loop the helper to update the arr
        # left pointer is used to track the left sorted array
        left = low_index
        # right pointer is used to track the right sorted array
        right = mid_index

        # we make sure low-high segment is sorted after merge
        # we will update the origin array for each cell
        for i in range(low_index, hig_index) : 
            if (left >= mid_index) : 
                # left portion used up. we keep moving right pointer until list filled up
                self.arr[i] = self.helper[right]
                right += 1
            elif (right >= hig_index) : 
                # right portion used up. we keep moving left pointer until list filled up 
                self.arr[i] = self.helper[left]
                left += 1
            # both pointer not reaching the end. we compare the value and pick
            # the smaller one
            elif (self.helper[left] < self.helper[right]) : 
                # left is smaller
                self.arr[i] = self.helper[left]
                left += 1
            else : 
                # right is smaller.
                self.arr[i] = self.helper[right]
                right += 1
        # in the end. arr[low_index : hig_index] is sorted
        
    def merge_sort(self, low_index, hig_index) : 
        if (hig_index - low_index <= 1) : 
            return 
        mid_index = (low_index + hig_index) // 2
        # both segments of arr will be sorted
        self.merge_sort(low_index, mid_index)
        self.merge_sort(mid_index, hig_index)
        # after the merge. the entire array will be sorted
        self.merge(low_index, mid_index, hig_index)

# test driver
arr = [random.randint(1,100) for i in range(10)]

print(arr)

s = sort_machine(arr)
s.merge_sort(0, len(arr))
print(arr)