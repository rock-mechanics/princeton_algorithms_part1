# question 2
# Search in a bitonic array. 
# An array is bitonic if it is comprised of an increasing sequence of integers 
# followed immediately by a decreasing sequence of integers. 
# Write a program that, given a bitonic array of nn distinct integer values, 
# determines whether a given integer is in the array.

# Standard version: Use ~3lgN compares in the worst case.
# Signing bonus: Use ~2lgN compares in the worst case 
# and prove that no algorithm can guarantee to 
# perform fewer than 2lgN compares in the worst case).

# the standard version
def search_bitonic(arr, number) : 
    # arr is bitonic
    # bitonic arr is distince integer array
    # it is increaseing then decreasing

    # find the largest index, this takes lgn
    largest_index = find_largest(arr, 0, len(arr))
    # search the first segment, this takes lgn
    # the sub array is increasing
    find_1 = qs(arr,True, 0, largest_index, number)
    # search the second segment, this takes lgn
    # the sub array is decreasing
    find_2 = qs(arr,False, largest_index + 1, len(arr), number)
    return find_1 or find_2

def quick_search_bitnoic_faster(arr, number) : 
    pass


def find_largest(arr, start_index, end_index) : 
    # this algorithm uses ~lgN
    # each branch is 
    current_index = (start_index + end_index) // 2
    if (current_index == end_index) : 
        return current_index
    elif (arr[start_index] > arr[start_index + 1]) : 
        # decreasing segment, dump the right
        return find_largest(arr, start_index, current_index)
    else : 
        # increasing segment, dump the left
        return find_largest(arr, current_index, end_index)

def qs(arr, increasing, start_index, end_index, number) : 
    # arr is sorted
    # 3 compares in total ~3lgN
    current_index = (start_index + end_index) // 2
    if (arr[start_index] == number) : 
        return True
    elif (start_index == end_index) : 
        return False
    elif (arr[current_index] > number) : 
        # decreasing segment, dump the right
        if increasing : 
            return qs(arr, increasing, start_index, current_index - 1, number)
        else : 
            return qs(arr, increasing, current_index + 1, end_index, number)
    else : 
        # increasing segment, dump the left
        if increasing : 
            return qs(arr, increasing, current_index + 1, end_index, number)
        else : 
            return qs(arr, increasing, start_index, current_index - 1, number)

def quick_search_bitonic(arr, start_index, end_index, number) : 
    current_index = (start_index + end_index) // 2
    pass




# generating a bitnoic array
arr = [i for i in range(9)]
for i in range(9) : 
    arr.append(9 - i)

# search the array
print(arr)
print('search for index of 4')
print(search_bitonic(arr, 9))
print('search for index of 10')
print(search_bitonic(arr, 10))