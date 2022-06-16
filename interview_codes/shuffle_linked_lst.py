# Shuffling a linked list. 
# Given a singly-linked list containing n items, 
# rearrange the items uniformly at random. 
# Your algorithm should consume a logarithmic (or constant) amount of extra memory 
# and run in time proportional to nlogn in the worst case.
import random

class node : 
    def __init__(self, number) : 
        self.value = number
        self.next = None

def printlst(arr) : 
    current = arr
    while current != None : 
        print(f'{current.value}', end = ' ') 
        current = current.next
    print()

def shuffle(arr) : 
    # use knuth method
    index = 1
    # starting from second node
    current = arr.next
    while current != None: 
        # randomly choose a node before it
        swap_index = random.randint(0, index - 1)
        # get the swap node
        swap_node = arr
        for i in range(swap_index) : 
            swap_node = swap_node.next 
        # swap the node value
        current.value , swap_node.value = swap_node.value, current.value
        # proceed to next node
        current = current.next
        index += 1

arr = node(0)
current = arr
for i in range(20) : 
    next = node(i)
    current.next = next
    current = current.next

printlst(arr)
shuffle(arr)
printlst(arr)