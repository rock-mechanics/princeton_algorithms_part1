# for compare tree
# on the leaves. all permutation must be included
# maybe there is even some duplicates
# so #number of leaves >= N!

# as we doubling the tree, the depth of the tree is h
# if we consider some branch will die early
# so #number of leaves <= 2**h

# chain the forumla
# 2 ** h >= N!
# we take lg on both side
# h >= lg(N!)
# lg(N!) = lg(N * (N-1) * (N-2) * .... * 2 * 1)
#        = lgN + lg(N-1) + lg(N-2) + .... + lg2 + lg1
#       <= lgN + lgN + lgN + .... + lgN + lgN
#       <= N * lgN
# h >= N*lgN
# on each level, there is at least 1 comparision
# conculstion : number of comparison is >= N*lgN

# this is the lower bound

# differnt algorithms have different uppper bound (worst case)
# for merge sort, in worst case, we do N*lgN
# so upper bound is N*lgN

# in this case, we have found the optimum algorithm
