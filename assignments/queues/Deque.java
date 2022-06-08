/* *****************************************************************************
 *  Name: Jing Chen
 *  Date: 06/07/2022
 *  Description:
 **************************************************************************** */

import edu.princeton.cs.algs4.StdOut;

import java.util.Iterator;

// to meet the memory requirement
// we need to use linked list
public class Deque<Item> implements Iterable<Item> {
    private Node firstNode;
    private Node lastNode;
    private int count;

    private class Node {
        public Item item = null;
        public Node previousNode = null;
        public Node nextNode = null;
    }

    // construct an empty deque
    public Deque() {
        count = 0;
        // create two null nodes
        firstNode = null;
        lastNode = null;
    }

    // is the deque empty?
    public boolean isEmpty() {
        return count == 0;
    }

    // return the number of items on the deque
    public int size() {
        return count;
    }

    // add the item to the front
    public void addFirst(Item item) {
        // corner case
        if (item == null) {
            throw new IllegalArgumentException();
        }
        count++;

        // create a new node
        Node newNode = new Node();
        newNode.item = item;

        // special case, two nodes are not connected
        if (count == 1) {
            firstNode = newNode;
            lastNode = newNode;
        }
        else {
            newNode.nextNode = firstNode;
            firstNode.previousNode = newNode;
            firstNode = newNode;
        }
    }

    // add the item to the back
    public void addLast(Item item) {
        // corner case
        if (item == null) {
            throw new IllegalArgumentException();
        }
        count++;

        Node newNode = new Node();
        newNode.item = item;

        // special case, two nodes are not connected
        if (count == 1) {
            firstNode = newNode;
            lastNode = newNode;
        }
        else {
            newNode.previousNode = lastNode;
            lastNode.nextNode = newNode;
            lastNode = newNode;
        }
    }

    // remove and return the item from the front
    public Item removeFirst() {
        if (count == 0) {
            throw new java.util.NoSuchElementException();
        }
        Item val = firstNode.item;
        firstNode = firstNode.nextNode;
        // special case, we consumed the last node
        if (firstNode == null) {
            lastNode = null;
        }
        else {
            // avoid loitering
            firstNode.previousNode = null;
        }
        count--;
        return val;
    }

    // remove and return the item from the back
    public Item removeLast() {
        if (count == 0) {
            throw new java.util.NoSuchElementException();
        }
        Item val = lastNode.item;
        lastNode = lastNode.previousNode;

        // special case, we consumed the first node
        if (lastNode == null) {
            firstNode = null;
        }
        else {
            // avoid loitering
            lastNode.nextNode = null;
        }
        count--;
        return val;
    }

    // return an iterator over items in order from front to back
    public Iterator<Item> iterator() {
        return new MyIterator();
    }

    // private class to implement the iterator
    // inner class is like a private method, it can be used with
    // any instance of outer instance object
    private class MyIterator implements Iterator<Item> {
        private Node currentNode;

        public MyIterator() {
            currentNode = firstNode;
        }

        public boolean hasNext() {
            return currentNode != null;
        }

        public Item next() {
            if (!hasNext()) {
                throw new java.util.NoSuchElementException();
            }
            Item val = currentNode.item;
            currentNode = currentNode.nextNode;
            return val;
        }

        public void remove() {
            throw new UnsupportedOperationException();
        }
    }

    public static void main(String[] args) {
        Deque<Integer> doubleQ = new Deque<>();
        StdOut.println("testing empty : " + doubleQ.isEmpty());
        StdOut.print("addFirst : size : ");
        // test add first + remove last
        for (int i = 0; i < 10; i++) {
            doubleQ.addFirst(i);
            StdOut.print(doubleQ.size() + " ");
        }
        StdOut.println("\ntesting empty : " + doubleQ.isEmpty());
        StdOut.print("removeLast : item : ");
        for (int i = 0; i < 10; i++) {
            StdOut.print(doubleQ.removeLast() + " ");
        }
        StdOut.println("\ntesting empty : " + doubleQ.isEmpty());
        // test add last + remove first
        StdOut.print("addLast : size : ");
        for (int i = 0; i < 10; i++) {
            doubleQ.addLast(i);
            StdOut.print(doubleQ.size() + " ");
        }
        StdOut.println("\ntesting empty : " + doubleQ.isEmpty());
        StdOut.print("removeFirst : item : ");
        for (int i = 0; i < 10; i++) {
            StdOut.print(doubleQ.removeFirst() + " ");
        }
        StdOut.println("\ntesting empty : " + doubleQ.isEmpty());

        StdOut.print("addFirst + addLast : size : ");
        // test add first + remove last
        for (int i = 0; i < 10; i++) {
            doubleQ.addFirst(i);
            doubleQ.addLast(i);
            StdOut.print(doubleQ.size() + " ");
        }
        StdOut.print("\ntesting iterator : ");
        for (int i : doubleQ) {
            StdOut.print(i + " ");
        }

        // auto-grader failed test
        StdOut.println();
        Deque<Integer> dq = new Deque<>();
        dq.addFirst(0);
        dq.removeFirst();
        dq.addFirst(0);
    }
}
