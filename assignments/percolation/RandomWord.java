/* *****************************************************************************
 *  Name:              Ada Lovelace
 *  Coursera User ID:  123456
 *  Last modified:     October 16, 1842
 **************************************************************************** */

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomWord {
    public static void main(String[] args) {
        int i = 1;
        String champion = "test";
        String word;
        while (!StdIn.isEmpty()) {
            word = StdIn.readString();
            if (StdRandom.bernoulli(1.0 / i)) {
                champion = word;
            }
            i++;
        }
        StdOut.println(champion);
    }
}
