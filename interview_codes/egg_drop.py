import math
# Egg drop. Suppose that you have an n-story building
# (with floors 1 through n) and plenty of eggs.
# An egg breaks if it is dropped from floor T or higher and does not break otherwise.
# Your goal is to devise a strategy to determine the value of  T
# given the following limitations on the number of eggs and tosses:

# number of floors
N = 1024000
T = 1024000
# Version 0: 1 egg, <=T tosses.
# sequential algorithm
def drop_version0(lower_floor, upper_floor, drop_number, broken_egg) : 
    current_floor = lower_floor
    for i in range(lower_floor, upper_floor + 1) : 
        current_floor = i
        drop_number += 1
        if drop_and_break(i) : 
            broken_egg += 1
            break
    return current_floor, drop_number, broken_egg
# Version 1: ~lgN eggs and ~lgN tosses.
# binary algorithm
def drop_version1(lower_floor, upper_floor, drop_number, eggs_broken) : 
    if (lower_floor == upper_floor) : 
        return lower_floor, drop_number, eggs_broken
    current_floor = (lower_floor + upper_floor) // 2
    is_break = drop_and_break(current_floor)
    if (is_break) : 
        return drop_version1(lower_floor, current_floor, drop_number + 1, eggs_broken + 1)
    else : 
        return drop_version1(current_floor + 1, upper_floor, drop_number + 1, eggs_broken)

# Version 2: ∼lgT eggs and ∼2lgT tosses.
# this algorithm can deal with targets in low range (low T) with large set N
def drop_version2() : 
    drop_number = 0
    eggs_broken = 0

    lower_bound = 1
    upper_bound = 1
    # find a range of slightly smaller than T elements
    # which contains the floor T
    # we break 1 egg to do the test
    # we tossed ~lgT times
    while (not drop_and_break(upper_bound)) : 
        lower_bound, upper_bound = upper_bound, upper_bound * 2
        drop_number += 1
    # only 1 egg is broken
    eggs_broken += 1
    # once we break the egg. we found the upper bound of the range
    # we use binary search to search the range, this will take ~lgT tosses
    # and will likely break ~lgT eggs
    # in total, we use ~2lgT tosses and breaks ~lgT eggs
    return drop_version1(lower_bound, upper_bound, drop_number, eggs_broken)

# Version 3: 2 eggs and  ∼2*sqrt(N) tosses.
def drop_version3() : 
    steps = int(math.sqrt(N))
    lower_bound = 1
    upper_bound = 1
    drop_number = 1
    # we find the a range of sqrt(N) elements which contains T
    while (not drop_and_break(upper_bound)) : 
        lower_bound, upper_bound = upper_bound, upper_bound + steps
        drop_number += 1
    # once the egg breaks. we found the range
    # we tossed at most sqrt(N) times
    # we do sequential tossing, at most we toss sqrt(N) times and break another egg 
    # in total we tossed 2*sqrt(N) times and breaks 2 eggs
    return drop_version0(lower_bound, upper_bound, drop_number, 1 )

# Version 4: 2 eggs and  <= csqrt(T) ​ tosses for some fixed constant c.
def drop_version4():
    # we first need to find sqrt(T), this will break 1 egg and toss sqrt(T) times
    estimate = 1
    drop_number = 1
    for i in range(1, N+1) : 
        drop_number += 1
        if (drop_and_break(i * i)) : 
            estimate = i
            break
    # sqrt(T) can be <= than our estimate
    # sqrt(T) is surly larger than estimate - 1 

    # we do sequential searching for the range
    lower_bound = (estimate - 1)**2
    upper_bound = estimate ** 2
    return drop_version0(lower_bound, upper_bound, drop_number, 1)

def drop_and_break(current_floor, isPrint = False): 
    if (isPrint) : 
        print(f"drop at {current_floor} : {current_floor >= T}")
    return current_floor >= T  

print()
print(f"N = {N} \t lgN = {int(math.log2(N))}\t sqrt(N) = {int(math.sqrt(N))}")
print(f"T = {T} \t lgT = {int(math.log2(T))}\t sqrt(T) = {int(math.sqrt(T))}")
print()
floor, drop_number, broken_egg = drop_version0(1, N, 0, 0)
print(f"using version 0 : floor {floor}, drops {drop_number} times, {broken_egg} broken")
floor, drop_number, broken_egg = drop_version1(1, N, 0, 0)
print(f"using version 1 : floor {floor}, drops {drop_number} times, {broken_egg} broken")
floor, drop_number, broken_egg = drop_version2()
print(f"using version 2 : floor {floor}, drops {drop_number} times, {broken_egg} broken")
floor, drop_number, broken_egg = drop_version3()
print(f"using version 3 : floor {floor}, drops {drop_number} times, {broken_egg} broken")
floor, drop_number, broken_egg = drop_version4()
print(f"using version 4 : floor {floor}, drops {drop_number} times, {broken_egg} broken")