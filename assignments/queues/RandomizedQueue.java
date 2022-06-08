/* *****************************************************************************
 *  Name: Jing Chen
 *  Date: 08/06/2022
 *  Description: Coursera
 **************************************************************************** */

import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

import java.util.Iterator;

public class RandomizedQueue<Item> implements Iterable<Item> {

    // internal data structure to hold elements
    private Item[] arr;
    // total available space in the array
    private int arrSize;
    // number of elements in the queue
    private int count;

    // construct an empty randomized queue
    public RandomizedQueue() {
        arr = (Item[]) new Object[1];
        arrSize = 1;
        count = 0;
    }

    // is the randomized queue empty?
    public boolean isEmpty() {
        return count == 0;
    }

    // return the number of items on the randomized queue
    public int size() {
        return count;
    }

    // add the item
    public void enqueue(Item item) {
        if (item == null) {
            throw new IllegalArgumentException();
        }
        if (count == arrSize) {
            resizeArr();
        }
        // push the item then increase the count
        arr[count++] = item;
    }

    // remove and return a random item
    public Item dequeue() {
        if (isEmpty()) throw new java.util.NoSuchElementException();
        int randomIndex = StdRandom.uniform(count);
        Item val = arr[randomIndex];
        // we place the last item into this slot
        // to make the arr continuous
        arr[randomIndex] = arr[--count];
        // avoid loitering
        arr[count] = null;

        // resize arr if arr is too empty
        if (count < arrSize / 4) {
            resizeArr();
        }
        // return the value.
        return val;
    }

    // return a random item (but do not remove it)
    public Item sample() {
        if (isEmpty()) throw new java.util.NoSuchElementException();
        int randomIndex = StdRandom.uniform(count);
        Item val = arr[randomIndex];
        return val;
    }

    // return an independent iterator over items in random order
    public Iterator<Item> iterator() {
        return new MyIterator();
    }

    private class MyIterator implements Iterator<Item> {

        // initialize the iterator index
        private RandomizedQueue<Item> tempQ = new RandomizedQueue<>();

        // constructor
        public MyIterator() {
            for (int i = 0; i < count; i++) {
                tempQ.enqueue(arr[i]);
            }
        }

        public boolean hasNext() {
            return !tempQ.isEmpty();
        }

        public Item next() {
            if (!hasNext()) throw new java.util.NoSuchElementException();
            return tempQ.dequeue();
        }

        public void remove() {
            throw new UnsupportedOperationException();
        }
    }

    private void resizeArr() {
        // this to take into account if there is zero elements
        // in this case resize to 1
        int newSize = count * 2 + 1;
        arrSize = newSize;
        Item[] newArr = (Item[]) new Object[newSize];

        // copy the old arr
        for (int i = 0; i < count; i++) {
            newArr[i] = arr[i];
        }
        // assign the reference
        arr = newArr;
    }

    // unit testing (required)
    public static void main(String[] args) {
        RandomizedQueue<Integer> rq = new RandomizedQueue<>();
        StdOut.println("empty test : " + rq.isEmpty());
        StdOut.print("size test  : ");
        for (int i = 0; i < 10; i++) {
            rq.enqueue(i);
            StdOut.print(rq.size() + " ");
        }
        StdOut.println("\nempty test : " + rq.isEmpty());

        StdOut.print("deqeue test : ");
        for (int i = 0; i < 10; i++) {
            StdOut.print(rq.dequeue() + " ");
        }
        StdOut.println("\nempty test : " + rq.isEmpty());

        // test the iterator
        for (int i = 0; i < 10; i++) {
            rq.enqueue(i);
        }

        StdOut.print("iterator test : ");
        for (int i : rq) {
            StdOut.print(i + " ");
        }
        StdOut.println("\nempty test : " + rq.isEmpty());

        StdOut.print("deqeue test : ");
        for (int i = 0; i < 10; i++) {
            StdOut.print(rq.dequeue() + " ");
        }
        StdOut.println("\nempty test : " + rq.isEmpty());
        StdOut.println();

        for (int i = 0; i < 4; i++) {
            rq.enqueue(i);
        }
        // testing nested iterator
        for (int i : rq) {
            for (int j : rq) {
                StdOut.println(i + ":" + j);
            }
        }

    }
}
