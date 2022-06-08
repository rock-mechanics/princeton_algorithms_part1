/* *****************************************************************************
 *  Name:              Jing Chen
 *  Coursera User ID:  123456
 *  Last modified:     May 27, 2022
 *****************************************************************************/

import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {

    private final int size;
    private final boolean[] sites;
    private final int startingAddress;
    private final int endingAddress;

    // boolean
    private boolean startingConnected = false;
    private boolean endingConnected = false;

    // the algorithm with a virtual top node and bottom node
    private final WeightedQuickUnionUF wuf;
    // the algorithm with a virtual top node
    private final WeightedQuickUnionUF wufTop;

    private int openSiteCount = 0;

    // creates n-by-n grid, with all sites initially blocked
    public Percolation(int n) {

        size = n;
        // corner case
        if (size <= 0) throw new IllegalArgumentException("size must be larger than zero");

        // we model the sites as a single array of nodes.
        // we place two extra nodes. top node and bottom node
        // top node is the first node, bottom node is the last node.
        // there will be n * n + 2 nodes in total
        // this network is used to check percolation
        wuf = new WeightedQuickUnionUF(size * size + 2);

        // since we use virtual top and botton node, there is a problem of back wash
        // https://www.cs.princeton.edu/courses/archive/spring19/cos226/assignments/percolation/checklist.php
        // to solve the problem, we need to maintain another network without connecting the bottom node.
        // this network is used to check whether site is full
        wufTop = new WeightedQuickUnionUF((size * size + 2));


        // we use a single sites array to keep track of the status of the sites
        // 0 -> blocked. 1 -> open
        // we block all the sites
        sites = new boolean[size * size + 2];
        for (int i = 0; i < sites.length; i++) {
            sites[i] = false;
        }

        // connect the first node with top row
        // connect the last node with bottom row
        startingAddress = 0;
        endingAddress = size * size + 1;
        for (int i = 1; i <= size; i++) {
            // for the normal wuf, we connect the virtual top node to first row.
            // for the normal wuf, we connect the virtual bottom node to bottom row.
            wuf.union(startingAddress, i);
            wuf.union(endingAddress, endingAddress - i);

            // to prevent back wash, we only connect the virtual top node to first row
            wufTop.union(startingAddress, i);
        }
    }

    // validate row / col index
    private boolean validateRowCol(int row, int col) {
        return row > 0 && row <= size && col > 0 && col <= size;
    }

    // the site address is one-dimensional array
    // the function finds the site address by row / col
    private int findAddress(int row, int col) {
        // check bounds of row/col index
        if (validateRowCol(row, col)) {
            return size * (row - 1) + col;
        }
        else {
            throw new IllegalArgumentException("Indexes must be within the size");
        }
    }

    // connect two sites for both algorithm network
    private void connectSite(int row1, int col1, int row2, int col2) {
        // check row and col are valid
        // if they are not valid, they cannot connect
        if (validateRowCol(row1, col1) && validateRowCol(row2, col2)) {
            int address1 = findAddress(row1, col1);
            int address2 = findAddress(row2, col2);
            // check if they are both open, if they are not open, they cannot connect
            if (isOpen(row1, col1) && isOpen(row2, col2)) {
                // connect both wuf
                wuf.union(address1, address2);
                wufTop.union(address1, address2);
            }
        }
    }

    // opens the site (row, col) if it is not open already
    public void open(int row, int col) {
        // check bounds of row/col index
        if (!validateRowCol(row, col))
            throw new IllegalArgumentException(
                    "Indexes must be within the size : " + row + " , " + col);

        // if the site is already open, skip it.
        if (isOpen(row, col)) return;

        // open the site
        int siteIndex = findAddress(row, col);
        sites[siteIndex] = true;

        // update the open site count
        openSiteCount++;

        // check if starting and ending connected
        // this is to prevent corner case, where this is only one site
        // percolation will give ture even if the site is blocked.
        if (row == 1) startingConnected = true;
        if (row == size) endingConnected = true;

        // find near sites
        int upperRow = row - 1;
        int lowerRow = row + 1;
        int leftCol = col - 1;
        int rightCol = col + 1;

        // connect near sites if they are open and valid
        connectSite(upperRow, col, row, col);
        connectSite(lowerRow, col, row, col);
        connectSite(row, leftCol, row, col);
        connectSite(row, rightCol, row, col);
    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col) {
        if (validateRowCol(row, col)) {
            return sites[findAddress(row, col)];
        }
        else {
            throw new IllegalArgumentException("row or col index is not valid");
        }
    }

    // is the site (row, col) full?
    public boolean isFull(int row, int col) {
        if (!isOpen(row, col)) return false;
        // to prevent back wash, we use the wufTop to find whether it is full
        return wufTop.find(startingAddress) == wufTop.find(findAddress(row, col));
    }

    // returns the number of open sites
    public int numberOfOpenSites() {
        return openSiteCount;
    }

    // does the system percolate?
    public boolean percolates() {
        // for single site. it does not percolates in the beginning
        // if they have the same root
        return startingConnected && endingConnected && wuf.find(startingAddress) == wuf
                .find(endingAddress);
    }

    // test client (optional)
    public static void main(String[] args) {
        int size = 20;
        double totalSites = size * size;
        StdOut.println("total sites : " + size * size);

        double totalProbability = 0;
        for (int i = 1; i < 1000; i++) {
            StdOut.println("Test " + i);
            Percolation p = new Percolation(size);
            // keep doing until it percolates
            while (!p.percolates()) {
                int row = StdRandom.uniform(1, size + 1);
                int col = StdRandom.uniform(1, size + 1);
                p.open(row, col);
            }
            double propablity = p.numberOfOpenSites() / totalSites;
            totalProbability += propablity;
            StdOut.println("percolates! " + p.numberOfOpenSites() + " probability : "
                                   + propablity + " average : " + totalProbability / i);
        }
    }
}
