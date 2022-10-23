/**
 * Author: Alex Wyner
 * Due Date: 10/28/22
 * Title: Programming Assignment 1: Closest Pair
 * 
 * Description: Using a bruteforce implementation and a Divide-and-Conquer 
 * recursive implementation, calculate the closest pair of points in an array 
 * of 2-dimensional points, comparing the runtimes of each implementation.
 */

import java.util.*;

public class ClosestPair
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		System.out.print("Enter a positive integer: ");
		int n = in.nextInt();

		Point[] p = new Point[n];
		fillPoints(p);
//		printPoints(p);
//		call on bruteForce and report results
//		bruteForce(p);

		mergeSort(p, 0, p.length-1);
//		call on rec_cl_pair and report results
		rec_cl_pair(p, 0, p.length-1);
//		printPoints(p);
		in.close();
	}

	// Method to populate array of type Point with random doubles between 0 and 
	// 1000, with the number of values generated given by the user 
	public static void fillPoints(Point[] p)
	{
		Random generator = new Random();
		for (int i = 0; i < p.length; i++)
		{
			double x = generator.nextDouble()*1000.0;
			double y = generator.nextDouble()*1000.0;
			p[i] = new Point(x, y);
		}
	}

	// Print x and y values of all points in array of type Point
	public static void printPoints(Point[] p)
	{
		for (int i = 0; i < p.length; i++)
		{
			System.out.println("(" + p[i].x + ", " + p[i].y + ")");
		}
	}

	// Bruteforce implementation to calculate closest points in array Point objects
	public static void bruteForce(Point[] p)
	{
		long startTime = System.nanoTime();

		double currDist;
		Point[] min = new Point[2];
		double minDist = eucDistance(p[0], p[1]);

		// Loop through each element in array p
		for (int x = 0; x < p.length; x ++)
		{
			// Loop through each element in array p
			for (int y = 0; y < p.length; y ++)
			{
				// Check that we are not comparing the same point to itself
				if (x != y)
				{
					// Compare distance between two points at index x and y of p
					currDist = eucDistance(p[x], p[y]);
					if (currDist < minDist)
					{
						minDist = currDist;
						min[0] = p[x];
						min[1] = p[y];
					}
				}
			}
		}
		long endTime = System.nanoTime();
		System.out.print("Points with minimum distance: ");
		System.out.print("(" + min[0].x + ", " + min[0].y + "), ");
		System.out.println("(" + min[1].x + ", " + min[1].y + ") ");
		System.out.println("Distance: " + minDist);
		System.out.println("Elapsed time: " + (endTime-startTime) + " nanoseconds");	
	}

	public static double rec_cl_pair(Point[] p, int i, int j)
	{
		i=0;
		j=2;
		if ((j - i) < 3) 		 // at most 3 points in p[i..j]
		{
			double delta;
			printPoints(p);
			p = sort_by_y(p, i, j);  // re-order p[i..j] by y-coordinate
			System.out.println("##########");
			printPoints(p);
			// delta = eucDistance(p[i], p[i+1]);
			/* if (j - i == 1)      // there are only two points
			return delta
			else
			return min(delta, distance(p[i+1], p[i+2]), distance(p[i], p[i+2])) */
		}
		   
		return 0;
	}

	private static Point[] sort_by_y(Point[] p, int i, int j) 
	{
		for (int y=0;y<3;y++)
		{
			for (int x=i; x<j; x++)
			{
				if (p[x].y > p[x+1].y)
				{
					Point temp = p[x];
					p[x] = p[x+1];
					p[x+1] = temp;
				}
			}
		}
		return p;
	}

	public static void mergeSort(Point[] p, int left, int right)
	{
		if (left == right)
			return;
		int middle = (left + right) / 2;
		mergeSort(p, left, middle);
		mergeSort(p, middle + 1, right);
		merge(p, left, middle, right);
	}

	public static void merge(Point[] p, int i, int k, int j)
	{
		Point[] temp = new Point[j-i+1];

		int c = 0;

		int l = i;
		int r = k+1;

		while (l <= k && r <= j)
		{
			if (p[l].x <= p[r].x)
			{
				temp[c] = new Point(p[l].x, p[l].y);
				c++;
				l++;
			}
			else
			{
				temp[c] = new Point(p[r].x, p[r].y);
				c++;
				r++;
			}
		}
		while (l <= k)
		{
			temp[c] = new Point(p[l].x, p[l].y);
			c++;
			l++;
		}
		while (r <= j)
		{
			temp[c] = new Point(p[r].x, p[r].y);
			c++;
			r++;
		}

		c = 0;
		for (int t = i; t <= j; t++)
		{
			p[t].x = temp[c].x;
			p[t].y = temp[c].y;
			c++;
		}
	}

	// Helper method to calculate Euclidean distance between two points
	public static double eucDistance(Point p, Point q)
	{
		return Math.sqrt(Math.pow(p.x-q.x, 2) + Math.pow(p.y-q.y, 2));
	}

	// Implementation to represent point on 2-dimensional plane
	public static class Point
	{
		private double x;
		private double y;

		Point(double a, double b)
		{
			x = a;
			y = b;
		}

		Point()
		{
			x = 0.0;
			y = 0.0;
		}

	}

}