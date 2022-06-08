import random

class custom_sort() : 
    def __init__(self, arr) :
        self.low = 0
        self.hig = len(arr) - 1
        self.arr = arr
        # count number of swaps and color peeking
        # maximum n calls for both function
        self.swaps = 0
        self.colors = 0

        # the arr will be like
        # r r r x w w w w x # # # # x b b b b
        # x is the pointer location 
        # # is the unscanned character
        # three pointers. the middle x is the scanning pointer i
    def custom_sort(self) : 
        i = 0
        while (i <= self.hig):
            # maximum n calls to color
            color = arr[i]
            self.colors += 1

            if (color == 'r') : 
                # maximum n calls to swap
                arr[i], arr[self.low] = arr[self.low], arr[i]

                self.swaps += 1
                # move the low pointer, invariants keep
                self.low += 1
                # move forward
                i += 1
                # print(arr)
                # we have swapped to the current location, which does not change the invarant
            elif (color == 'b') : 
                arr[i], arr[self.hig] = arr[self.hig], arr[i]
                self.swaps += 1
                self.hig -= 1
                # don't move forward, check the swapped item
                # because the invariants broken.
                # print(arr)
            else: 
                # move forward
                # invariants keep
                i += 1
                # print(arr)

arr = [random.choice(['r','b','w']) for i in range(10)]
print(arr)
s = custom_sort(arr)
s.custom_sort()
print(arr)
print(f"{s.swaps} swaps and {s.colors} color peeking")