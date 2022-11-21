import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class KnapSack
{
    public static void main(String[] args) throws FileNotFoundException
    {
        File f = new File("D:\\College\\3-Junior\\Semester-1\\Junior-git\\CS-366\\knapsack\\input.txt");
        Scanner scan = new Scanner(f);

        // Parse input file into number of items n, capacity c, and array of sizes S
        int n = Integer.parseInt(scan.nextLine());
        int c = Integer.parseInt(scan.nextLine());
        int[] S = new int[n];

        for (int i = 0; i < n; i++)
        {
            S[i] = Integer.parseInt(scan.nextLine());
        }

        dynamicKnapSack(S, c);
    //  backtrackKnapSack(S, c);
        scan.close();
    }

    public static void dynamicKnapSack(int[] S, int c)
    {
        long start = System.nanoTime();
        long end;
        int n = S.length;
        boolean exist[][] = new boolean[n][c];
        boolean belong[][] = new boolean[n][c];

        exist[0][0] = true;
        for (int j = 1; j < c; j++)
        {
            exist[0][j] = false;
        }
        
        for (int i = 1; i < n; i++)
        {
            for (int j = 0; j < c; j++)
            {
                exist[i][j] = false;
                if (exist[i-1][j])
                {
                    exist[i][j] = true;
                    belong[i][j] = false;
                }
                else if (j - S[i] >= 0)
                {
                    if (exist[i-1][j-S[i]])
                    {
                        exist[i][j] = true;
                        belong[i][j] = true;
                    }
                }
            }
        }
        end = System.nanoTime();
        System.out.println("Time in nanoseconds: " + (end-start));
        // Print solution
        for (int i = 0; i < n; i ++)
        {
            for (int j = 0; j < c; j++)
            {
                System.out.print(exist[i][j] + "\t");
            }
            System.out.println();
        }

    }
}