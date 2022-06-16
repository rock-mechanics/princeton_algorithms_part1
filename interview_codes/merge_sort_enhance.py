import random

class sort_machine : 
    def __init__(self) : 
        pass

    # after this merge, aux will be fully sorted
    # arr will be half sorted
    def merge(self, arr, aux, low_index, mid_index, hig_index) : 
        # we assume first one is partially sorted
        left = low_index
        right = mid_index
        for i in range(low_index, hig_index) : 
            if (left >= mid_index) : 
                aux[i] = arr[right] 
                right += 1
            elif (right >= hig_index) : 
                aux[i] = arr[left]
                left += 1
            elif (arr[left] < arr[right]) : 
                aux[i] = arr[left]
                left += 1
            else : 
                aux[i] = arr[right]
                right += 1

    def merge_sort(self, arr, aux, low, hig) : 
        # in recursion, we can make assumtions boldly
        # assumption : arr is fully sorted after merge_sort.
        # assumption : aux is half sorted after merge_sort
        # in the end, we must prove our assumption is true

        # base case, one element, no need to sort any more
        if (hig - low <= 1) : 
            return

        mid = (low + hig) // 2

        self.merge_sort(aux, arr, low, mid)
        self.merge_sort(aux, arr, mid, hig)
        # after thest two ops, 
        # aux is half sorted. as it is fully sorted each step
        # arr is quaterly sorted.

        # we need to make sure arr is fully sorted to confirm the assumption
        # the merge takes a halfly sorted aux.
        # fully sort the arr
        self.merge(aux, arr, low, mid, hig)
        # now we confirm to our assumption.
        # aux is half sorted. arr is ful sorted

arr = [random.randint(0,100) for i in range(10)]
aux = arr[:]

s = sort_machine()

s.merge_sort(arr, aux, 0, len(arr))

print(arr)
print(aux)