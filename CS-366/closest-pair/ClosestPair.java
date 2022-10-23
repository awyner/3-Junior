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

		mergeSort(p, 0, p.length-1);
//		call on rec_cl_pair and report results
//		printPoints(p);
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

	public static double bruteForce(Point[] p)
	{

	}

	public static double rec_cl_pair(Point[] p, int i, int j)
	{

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