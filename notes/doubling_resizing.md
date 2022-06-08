# resize array effectively

## resize cost

each resize, the array has to 
* create a new array -- **(no cost)**
* copy the old array -- **(with cost)**

for a array of size `N`, copying all elements takes `N` array accesses

## inefficienty resize
we increase the array by 1 when array overflow

```
Array Items  :   1 2 3 4 5 6 7 8 .... N
Resize Cost  :   x 2 3 4 5 6 7 8 .... N  ~ (1/2)N*N
```

* the algorithm is not scallable

## double resize
when array overflow, we double the array

```
Doubling     :    x   x       x      x
Array Items  :  1 2 3 4 5 6 7 8 .... N
Resize Cost  :  x 2 x 4 x x x 8 .... N  
```
## Number of array access for array N
```
2 + 4 + 8 + .... + N array access
```
* this is a geometric series

## Cost of array doubling
* calculate the sum
```
2 + 4 + 8 + .... + N = S
    2 + 4 + 8 + .... + N + 2N = 2S
```
* if we minus term 2 with term 1
```
S = 2N 
```
## Amazing
* the cost drops from ~1/2N*N to 2N
* great improvement