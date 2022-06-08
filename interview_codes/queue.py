# Implement a queue with two stacks 
# so that each queue operations takes a constant 
# amortized number of stack operations. 

# a simple stack 
# not the purpose of this exercise
class my_stack : 
    def __init__(self) : 
        self.numbers = []
        self.count = 0
    def push(self, number) : 
        self.numbers.append(number)
        self.count += 1
    def pop(self) : 
        if self.count == 0 : 
            raise
        self.count -= 1
        return self.numbers.pop()

# the queue will pour elements from time to time only when there is a switch 
# between enqueue and dequeue. the distance between two dequeue operation is the steps taken
# so it will be very small indeed

# operations e e e e d e e d e e d e d e e e d d d 
# steps      1 1 1 1 5 1 1 3 1 1 3 1 2 1 1 1 4 1 1 

class my_queue : 
    def __init__(self) : 
        self.stack = my_stack()
        self.reverse_stack = my_stack()
    def enqueue(self, number) : 
        self.stack.push(number)
    def dequeue(self) : 
        # if there is no element in our reverse stack
        # we pour the stack to the reverse stack
        if self.reverse_stack.count == 0 : 
            while self.stack.count > 0 : 
                self.reverse_stack.push(self.stack.pop())
        # if there is elements in the reverse stack
        # the top of the reverse stack is the oldest element
        return self.reverse_stack.pop()

q = my_queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)

for i in range(6) : 
    print(q.dequeue())