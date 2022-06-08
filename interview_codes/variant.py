# covariant vs contra variant

# sub typing
# cat <: animal
# it reads cat is less general than animal
# cat is a subtype of animal

# composite types may be tricky 
# variance is about how composite of T is related to T, in terms of subtyping
# to simplify
# list of cat vs list of animal

# in java. arrays are convariant
# base type : String <: Object
# comp type : String[] <: Object[]
# we can say 
# 1. String is Object
# 2. String Array is Object Array
# so a list of object 
# [ object, string, object, string, string ]
# the direction flow is the same


# In Java, it is a bit tricky
# Assume generic array is possible
# [box<chicken>, box<chicken>, box<chicken>] is array of box of chicken : pass
# [box<chicken>, box<chicken>, box<chicken>] is array of object : pass
# [int, box<chicken>, box<chicken>] is array of object : pass 

print('type system has passed all the type check')
print('we still has a type error')
# boxes[0].lay_eggs()  : error