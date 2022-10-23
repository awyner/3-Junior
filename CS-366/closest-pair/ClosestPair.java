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
		printPoints(p);
//		System.out.println(eucDistance(p[0], p[1]));
//		call on bruteForce and report results
		bruteForce(p);

		mergeSort(p, 0, p.length-1);
//		call on rec_cl_pair and report results
//		printPoints(p);
		in.close();
	}

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

	public static void printPoints(Point[] p)
	{
		for (int i = 0; i < p.length; i++)
		{
			System.out.println("(" + p[i].x + ", " + p[i].y + ")");
		}
	}

	public static void bruteForce(Point[] p)
	{
		long startTime = System.nanoTime();
		Point[] min = new Point[2];
		double currDist;
		double minDist = eucDistance(p[0], p[1]);
		for (int x = 0; x < p.length; x ++)
		{
			for (int y = 1; y < p.length; y ++)
			{
				currDist = eucDistance(p[x], p[y]);
				System.out.println(minDist + " | " + currDist);
				if (Math.min(currDist, minDist) != minDist && x != y)
				{
					minDist = currDist;
					min[0] = p[x];
					min[1] = p[y];
				}
			}
		}
		long endTime = System.nanoTime();
		printResults(min, minDist, startTime, endTime);
	}

	// TODO
	public static double rec_cl_pair(Point[] p, int i, int j)
	{
		return 0;
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

	public static double eucDistance(Point p, Point q)
	{
		return Math.sqrt(Math.pow(p.x-q.x, 2) + Math.pow(p.y-q.y, 2));
	}

	private static void printResults(Point[] min, double minDist, long startTime, long endTime) {
		System.out.print("Points with minimum distance: ");
		System.out.print("(" + min[0].x + ", " + min[0].y + "), ");
		System.out.println("(" + min[1].x + ", " + min[1].y + ") ");
		System.out.println("Distance: " + minDist);
		System.out.println("Elapsed time: " + (endTime-startTime) + " nanoseconds");
	}

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