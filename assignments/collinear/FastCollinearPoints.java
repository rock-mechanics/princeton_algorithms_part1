/* *****************************************************************************
 *  Name: Jing Chen
 *  Date: Jun 15, 2022
 *  Description: Coursera
 **************************************************************************** */

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;

import java.util.Arrays;

public class FastCollinearPoints {
    private int lineCounts = 0;
    private final LineArray segments = new LineArray(null);
    private LineArray currentSegment = segments;

    // we don't know how many line segments are there
    // we create a linked list data structure to hold them
    private class LineArray {

        LineSegment content = null;
        LineArray next = null;

        public LineArray(LineSegment seg) {
            content = seg;
        }
    }

    // finds all line segments containing 4 or more points
    public FastCollinearPoints(Point[] points) {
        // check input
        if (points == null) {
            throw new IllegalArgumentException();
        }
        for (Point point : points) {
            if (point == null) {
                throw new IllegalArgumentException();
            }
        }
        // check duplicates
        for (int i = 0; i < points.length; i++) {
            for (int j = i + 1; j < points.length; j++) {
                if (points[i].compareTo(points[j]) == 0) {
                    throw new IllegalArgumentException();
                }
            }
        }
        // if points are not enough, exit.
        if (points.length < 4) return;

        // we keep a copy of the points
        Point[] ps = new Point[points.length];
        for (int i = 0; i < points.length; i++) {
            ps[i] = points[i];
        }
        // for each point, we try to find the collinear point
        // if they are collinear with p, then the slope should be the same
        int pointCount;
        double currentSlope;
        for (Point p : points) {
            // we first sort based on its natural order
            Arrays.sort(ps);
            // then we sort it based on the slope
            // the sort algorithm is stable, so its order should be preserved
            Arrays.sort(ps, p.slopeOrder());
            // we loop through the point to find the collinar points
            // the first point is the point itself
            // we skip the first point
            // we assume the second point form a colliear line, we got two points in the line
            currentSlope = ps[1].slopeTo(ps[0]);
            pointCount = 2;
            for (int i = 2; i < ps.length; i++) {
                if (Double.compare(ps[i].slopeTo(ps[0]), currentSlope) == 0) {
                    pointCount++;
                }
                else {
                    if (pointCount >= 4) {
                        Point[] collinars = new Point[pointCount];
                        collinars[0] = ps[0];
                        int startingIndex = i - pointCount;
                        for (int j = 1; j < pointCount; j++) {
                            collinars[j] = ps[startingIndex + j];
                        }
                        addSegment(collinars);
                        // we need to continue searching for further collinear points
                    }
                    // if points is not enough, or if we have already added one line
                    // we reset the count and slope
                    pointCount = 2;
                    currentSlope = ps[i].slopeTo(ps[0]);
                }
            }
            // we may go over the last segment
            if (pointCount >= 4) {
                Point[] collinars = new Point[pointCount];
                collinars[0] = ps[0];
                int startingIndex = ps.length - pointCount;
                for (int j = 1; j < pointCount; j++) {
                    collinars[j] = ps[startingIndex + j];
                }
                addSegment(collinars);
            }
        }
    }

    // the number of line segments
    public int numberOfSegments() {
        return lineCounts;
    }

    private void addSegment(Point[] points) {
        // we make sure the first point is the smallest one
        for (int i = 1; i < points.length; i++) {
            if (points[0].compareTo(points[i]) > 0) {
                // not the two end points
                return;
            }
        }
        LineSegment line = new LineSegment(points[0], points[points.length - 1]);
        lineCounts++;
        LineArray arr = new LineArray(line);
        currentSegment.next = arr;
        currentSegment = currentSegment.next;
    }

    // the line segments
    public LineSegment[] segments() {
        LineSegment[] returnSegments = new LineSegment[lineCounts];
        // we loop from start
        currentSegment = segments;
        for (int i = 0; i < lineCounts; i++) {
            returnSegments[i] = currentSegment.next.content;
            currentSegment = currentSegment.next;
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
        FastCollinearPoints collinear = new FastCollinearPoints(points);
        for (LineSegment segment : collinear.segments()) {
            StdOut.println(segment);
            segment.draw();
        }
        StdDraw.show();

        StdOut.println(collinear.numberOfSegments());
    }
}
