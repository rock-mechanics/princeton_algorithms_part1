/* *****************************************************************************
 *  Name:              Jing Chen
 *  Coursera User ID:  123456
 *  Last modified:     May 27 2022
 **************************************************************************** */

import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {

    private static final double CONFIDENCE_95 = 1.96;
    private final double[] openFractions;

    // constructor
    public PercolationStats(int n, int trials) {
        // corner cases
        if (n <= 0 || trials <= 0) {
            throw new IllegalArgumentException(
                    "grid size and trials must be larger than zero " + n + ", " + trials);
        }
        openFractions = new double[trials];

        // we start to do the sampling
        double totalSites = n * n;
        for (int i = 0; i < trials; i++) {
            Percolation p = new Percolation(n);
            // keep doing until it percolates
            while (!p.percolates()) {
                int row = StdRandom.uniform(1, n + 1);
                int col = StdRandom.uniform(1, n + 1);
                p.open(row, col);
            }
            openFractions[i] = p.numberOfOpenSites() / totalSites;
        }
    }

    // sample mean of percolation threshold
    public double mean() {
        return StdStats.mean(openFractions);
    }

    // sample standard deviation of percolation threshold
    public double stddev() {
        return StdStats.stddev(openFractions);
    }

    // low endpoint of 95% confidence interval
    public double confidenceLo() {
        return mean() - CONFIDENCE_95 * stddev() / Math.sqrt(openFractions.length);
    }

    // high endpoint of 95% confidence interval
    public double confidenceHi() {
        return mean() + CONFIDENCE_95 * stddev() / Math.sqrt(openFractions.length);
    }

    // test client (see below)
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int t = Integer.parseInt(args[1]);

        PercolationStats p = new PercolationStats(n, t);
        StdOut.println("mean\t= " + p.mean());
        StdOut.println("stddev\t= " + p.stddev());
        StdOut.println(
                "95% confidence interval\t=  [" + p.confidenceLo() + ", " + p.confidenceHi() + "]");
    }
}
