import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;

public class BruteCollinearPoints {
    private int lineCount = 0;
    private final LineSegment[] lineSegments;

    // finds all line segments containing 4 points
    public BruteCollinearPoints(Point[] points) {
        // check input
        if (points == null) {
            throw new IllegalArgumentException();
        }
        for (Point point : points) {
            if (point == null) {
                throw new IllegalArgumentException();
            }
        }
        // create a temporary array to hold
        lineSegments = new LineSegment[points.length];

        // check duplicates
        for (int i = 0; i < points.length; i++) {
            for (int j = i + 1; j < points.length; j++) {
                if (points[i].compareTo(points[j]) == 0) {
                    throw new IllegalArgumentException();
                }
            }
        }
        Point minPoint, maxPoint;
        for (int i = 0; i < points.length - 3; i++) {
            for (int j = i + 1; j < points.length - 2; j++) {
                for (int k = j + 1; k < points.length - 1; k++) {
                    for (int h = k + 1; h < points.length; h++) {
                        // we determine whether they are collinear
                        double slope1 = points[i].slopeTo(points[j]);
                        double slope2 = points[i].slopeTo(points[k]);
                        double slope3 = points[i].slopeTo(points[h]);
                        // check the three slopes
                        if (Double.compare(slope1, slope2) == 0
                                && Double.compare(slope1, slope3) == 0) {
                            // we found a linear line, now find the max and min point
                            minPoint = points[i];
                            minPoint = points[j].compareTo(minPoint) < 0 ? points[j] : minPoint;
                            minPoint = points[k].compareTo(minPoint) < 0 ? points[k] : minPoint;
                            minPoint = points[h].compareTo(minPoint) < 0 ? points[h] : minPoint;

                            maxPoint = points[i];
                            maxPoint = points[j].compareTo(maxPoint) > 0 ? points[j] : maxPoint;
                            maxPoint = points[k].compareTo(maxPoint) > 0 ? points[k] : maxPoint;
                            maxPoint = points[h].compareTo(maxPoint) > 0 ? points[h] : maxPoint;

                            lineSegments[lineCount++] = new LineSegment(minPoint, maxPoint);
                        }
                    }
                }
            }
        }
    }

    // the number of line segments
    public int numberOfSegments() {
        return lineCount;
    }

    // the line segments
    public LineSegment[] segments() {
        LineSegment[] returnSegments = new LineSegment[lineCount];
        for (int i = 0; i < returnSegments.length; i++) {
            returnSegments[i] = lineSegments[i];
        }
        return returnSegments;
    }

    public static void main(String[] args) {
        // read the n points from a file
        In in = new In(args[0]);
        int n = in.readInt();
        Point[] points = new Point[n];
        for (int i = 0; i < n; i++) {
            int x = in.readInt();
            int y = in.readInt();
            points[i] = new Point(x, y);
        }

        // draw the points
        StdDraw.enableDoubleBuffering();
        StdDraw.setXscale(0, 32768);
        StdDraw.setYscale(0, 32768);
        for (Point p : points) {
            p.draw();
        }
        StdDraw.show();

        // print and draw the line segments
        BruteCollinearPoints collinear = new BruteCollinearPoints(points);
        for (LineSegment segment : collinear.segments()) {
            StdOut.println(segment);
            segment.draw();
        }
        StdDraw.show();
    }
}
