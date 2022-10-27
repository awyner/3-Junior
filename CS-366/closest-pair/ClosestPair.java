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
		bruteForce(p);

		mergeSort(p, 0, p.length-1);
//		call on rec_cl_pair and report results
		long startTime=System.nanoTime();
		System.out.println("\nDivide and Conquer: \nMinimum Distance: " + rec_cl_pair(p, 0, p.length-1));
		long endTime=System.nanoTime();
		System.out.println("Elapsed time: " + (endTime-startTime) + " nanoseconds");
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
		for (int x = 0; x < p.length; x ++)   // O(n)
		{
			// Loop through each element in array p
			for (int y = 0; y < p.length; y ++) // O(n^2)
			{
				// Check that we are not comparing the same point to itself
				if (x != y)      
				{
					// Compare distance between two points at index x and y of p
					currDist = eucDistance(p[x], p[y]);  // O(1)
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
		System.out.print("\nBrute force:\nPoints with minimum distance: ");
		System.out.print("(" + min[0].x + ", " + min[0].y + "), ");
		System.out.println("(" + min[1].x + ", " + min[1].y + ") ");
		System.out.println("Minimum Distance: " + minDist);
		System.out.println("Elapsed time: " + (endTime-startTime) + " nanoseconds");	
	}

	public static double rec_cl_pair(Point[] p, int i, int j)
	{
		int m;
		double line;
		double deltaL;
		double deltaR;
		double delta;
		Point[] v = new Point[p.length];
		
		if ((j - i) < 3) 			 // at most 3 points in p[i..j]
		{

			p = sort_by_y(p, i, j);  // re-order p[i..j] by y-coordinate
			delta = eucDistance(p[i], p[i+1]);

			if (j - i == 1){      	 // there are only two points
				return delta;
			} else {
				return Math.min(delta, Math.min(eucDistance(p[i+1], p[i+2]), eucDistance(p[i], p[i+2])));
			}
		}
		m = (i + j)/2;
		line = p[m].x; 						// line = middle of p[i..j] by x-values
		deltaL = rec_cl_pair(p, i, m);		// deltaL = min distance of left half
		deltaR = rec_cl_pair(p, m+1, j); 	// deltaR = min distance of right half
		delta = Math.min(deltaL, deltaR); 	// smallest distance of the two halves
		merge_by_y(p, i, m, j); 		// merge so that p[i..j] is sorted by y
		
		// Of points in p[i..j], find points in vertical strip of width 2*delta,
 		// centered at line, store in temp array v, and t = number of pts
		int t = 0;
		for (int k=i; k<j; k++) 
		{
			if (p[k].x > line - delta && p[k].x < line + delta)
			{
	//			t = t + 1;
				v[t] = p[k];
			}
	 	}
		// Find closest pair among points in array v. NOTE: Cool math shows
		// each point in the strip only needs to be compared to, at most,
		// the next 7 other points. Any others are further away than delta.
		for (int k = 0; k < t-1; k++)
		{
			for (int s = k+1; s < Math.min(t,k+7); s++) // inner loop iterates <= 7 times
				delta = Math.min(delta, eucDistance(v[k],v[s]));
		}

		return delta;
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

	public static void merge_by_y(Point p[], int i, int k, int j)
	{
		Point[] temp = new Point[j-i+1];

		int c = 0;

		int l = i;
		int r = k+1;

		while (l <= k && r <= j)
		{
			if (p[l].y <= p[r].y)
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