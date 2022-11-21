import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class KnapSack
{
    public static int n;
    public static int c;
    public static int[] S;
    public static int maxSize = 0;
    public static int[] maxSubset;
    public static void main(String[] args) throws FileNotFoundException
    {
        //File f = new File("D:\\College\\3-Junior\\Semester-1\\Junior-git\\CS-366\\knapsack\\input.txt");
        File f = new File("C:\\Users\\alexw\\Documents\\classwork\\3-Junior\\CS-366\\knapsack\\input.txt");
        Scanner scan = new Scanner(f);

        // Parse input file into number of items n, capacity c, and array of sizes S
        n = Integer.parseInt(scan.nextLine());
        c = Integer.parseInt(scan.nextLine());
        S = new int[n];

        for (int i = 0; i < n; i++)
        {
            S[i] = Integer.parseInt(scan.nextLine());
        }
        dynamicKnapSack();
        backtrackKnapSack();
        scan.close();
    }

    public static void dynamicKnapSack()
    {
        long start = System.nanoTime();
        long end;
        boolean exist[][] = new boolean[n+1][c+1];
        boolean belong[][] = new boolean[n+1][c+1];

        exist[0][0] = true;
        for (int j = 1; j < c; j++)
        {
            exist[0][j] = false;
        }
        
        for (int i = 1; i <= n; i++)
        {
            for (int j = 0; j <= c; j++)
            {
                exist[i][j] = false;
                if (exist[i-1][j])
                {
                    exist[i][j] = true;
                    belong[i][j] = false;
                }
                else if (j - S[i-1] >= 0)
                {
                    if (exist[i-1][j-S[i-1]])
                    {
                        exist[i][j] = true;
                        belong[i][j] = true;
                    }
                }
            }
        }
        printSolution(belong, exist);
        end = System.nanoTime();
        System.out.println("Time in nanoseconds: " + (end-start));
    }

    public static void backtrackKnapSack()
    {
        maxSubset = new int[n];
        int[] subset = new int[n];
        rbacktrackKnapSack(1, n, subset);
        System.out.println(maxSize);
    }

    public static void rbacktrackKnapSack(int k, int l, int[] subset)
    {
        for (int j = 0; j <=1; j++)
        {
            subset[k] = j;
            if (k == n)
            {
                checkSubset(subset);
            }
        }
        
    }
    
    public static void checkSubset(int[] subset)
    {
        int[] currSubset = new int[n];
        int total = 0;

        for (int x = 0; x < n; x++)
        {
            if (subset[x] == 1)
            {
                currSubset[x] = S[x];
                total += S[x];
            }
        }
        if (total > maxSize)
        {
            maxSize = total;
            for (int x = 0; x < currSubset.length; x++){ maxSubset[x] = currSubset[x]; }
        }
    }

    public static void printSolution(boolean[][] belong, boolean[][] exists)
    {
        int total = 0;
        int i = n;
        int j = c;
        System.out.println("Items Selected:");
        while (j > 0)
        {
            if (exists[i][j])
            {
                if (belong[i][j])
                {
                    System.out.println("Item " + i + ", Size = " + S[i-1] + " ");
                    total+=S[i-1];
                    j-= S[i-1];
                    i--;
                } else {
                    i--;
                }
            } else {
                j--;
            }
        }
        System.out.println("Capacity: " + c + "\nTotal space used: " + total);
    }
}