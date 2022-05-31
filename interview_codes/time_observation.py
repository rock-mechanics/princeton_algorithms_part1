# standard version

import math
import time;

def quadratic_function(n) : 
    test = 0
    for i in range(n) : 
        for j in range(n) : 
            test = i + j

# testing array
size = 10
previous_duration = 1

# print the header
print ("size\tdur\tdur_q\tdur_lg_q")
# do tests
# the test can only scale 10 times
for i in range(10) : 
    # double the size of the array
    size = size * 2
    start = time.perf_counter()
    quadratic_function(size)
    end = time.perf_counter()
    duration = end - start
    duration_quotion = duration / previous_duration
    previous_duration = duration
    duration_lg_quotion = math.log2(duration_quotion)
    print (f"{size}\t{duration:.2E}\t{duration_quotion:.2}\t{duration_lg_quotion:.2}")