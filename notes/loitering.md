# loitering

## Java garbage collection
when a object is no longer refereced, the garbage collector will use the memeory for other purposes.

## Loitering
滞留
an object is no longer needed, but somehow, we still keep a reference to it. then the garbage collection cannot reclaim the memory

## Example
Stack Implementaion
```
stack.pop();
```
```
stack.current_index--
```
* if we use an array as a stack, the old `stack_array[current_index]` is no longer needed.but the reference still kept in the array

```
stack_array[stack.current_index] = null
stack.current_index--
```
* assigning the item to `null`, release the reference of the object