# Stack with max. 
# Create a data structure that efficiently supports the stack operations (push and pop) 
# and also a return-the-maximum operation. 
# Assume the elements are real numbers so that you can compare them.

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
            raise Exception("stack is empty.")
        self.count -= 1
        return self.numbers.pop()

# we keep track of the maximum of the stack
# at each state of the stack
# we use another stack to sync with the data stack
class stack_max : 
    def __init__(self) : 
        self.stack = my_stack()
        self.max_stack = my_stack()
    def push(self, number) : 
        # push the number first
        self.stack.push(number)
        # if max stack is empty, we simply push the number
        if self.max_stack.count == 0 : 
            self.max_stack.push(number)
        else : 
            # check the previous maximum in the max stack
            previous_max = self.max_stack.pop()
            # once got the value, we have to push it back to sync with previous stack state
            self.max_stack.push(previous_max) 
            # the stack grows, we need to push a new max value
            if number > previous_max : 
                self.max_stack.push(number)
            else : 
                self.max_stack.push(previous_max)
    def pop(self) : 
        # we pop the max as well. because it is the max of current stack state
        self.max_stack.pop()
        return self.stack.pop()
    def max(self) : 
        # get the max of current stack state
        max_number = self.max_stack.pop()
        # push it back
        self.max_stack.push(max_number)
        # return the value
        return max_number

s = stack_max()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(6)
s.push(6)
s.push(7)
s.push(8)

print(f"pop {s.pop()} : max {s.max()}")
print(f"pop {s.pop()} : max {s.max()}")
print(f"pop {s.pop()} : max {s.max()}")
print(f"pop {s.pop()} : max {s.max()}")
print(f"pop {s.pop()} : max {s.max()}")