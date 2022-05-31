# Successor with delete. 
# Given a set of N integers S={0,1,…,N−1} and a sequence of requests of the following form:
# Remove x from S 
# Find the successor of x: 
# the smallest y in S such that y≥x. 
# design a data type so that all operations (except construction) should take logarithmic time or better.
class uf_successor_del : 
    def __init__(self, size) : 
        self.size = size
        # keep track of the root of each node
        self.roots = [ n for n in range(size)]
        # keep track of the successor
        # the successor of the top node is the successor all its children node
        # when inquire the successor, we find the top node and check the successor
        # in the beginning, the top node is the node iteself
        # in the beginning, the successor is the node iteself (>= relationship)
        self.successor = [ n for n in range(size)]
        # the weight of each sub tree
        # we totally follow the quick-union-find-weighted algorithm
        self.weight = [1 for n in range(size)]
    
    def __str__(self) : 
        return ' '.join([str(n) for n in self.roots])
    
    def root(self, i) : 
        while (self.roots[i] != i) : 
            # tree compressing
            # skip the parent, connect the grand parent
            self.roots[i] = self.roots[self.roots[i]]
            # become the parent
            i = self.roots[i]
        return i
    
    def connected(self, i, j) : 
        return self.roots[i] == self.roots[j]
    
    def union(self, i, j) : 
        root_i = self.roots[i]
        root_j = self.roots[j]
        if (self.weight[root_i] > self.weight[root_j]) : 
            self.roots[root_j] = root_i
            self.weight[root_i] += self.weight[root_j]
            # new code
            # the roots[larger value] is attached under the roots[lower value]
            # the successor is not correct now. we need to update the successor to make sure
            # it is the successor of the whole branch
            self.successor[root_i] = self.successor[root_j]
        else : 
            self.roots[root_i] = root_j
            self.weight[root_j] += self.weight[root_i]
            # the roots[smaller value] is attached under the roots[larger value]
            # the successor is correct, no need to modify
    
    def find_successor(self, i) : 
        # the root contains the successor for the whole branch
        root_i = self.root(i)
        return self.successor[root_i]
    
    # above are the standard union-find-weighted-compression algorithm
    # now we implement the custom union 

    def remove(self, i) : 
        # if i is not the largest node
        if (i < self.size - 1) : 
            # we simply put it under its next node
            # this will attach i to the root of i + 1
            # or it will attach the 
            self.union(i, i + 1)
        else : 
            # if this is the largest node
            # we update its successor as -1 to indicate there is no successor
            self.successor[self.size - 1] = -1


# test driver code
uf = uf_successor_del(10)
uf.remove(4)
uf.remove(5)
uf.remove(6)
print(uf.find_successor(4))
print(uf.find_successor(5))
print(uf.find_successor(6))

# remove last value
uf.remove(9)
print(uf.find_successor(9))
uf.remove(8)
print(uf.find_successor(8))

