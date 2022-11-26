/**
 * Author: Alex Wyner
 * Due Date: 12/2/22
 * Title: Programming Assignment 2: Knapsack Problem
 * 
 * Description: Using dynamic programming and backtracking, determine which 
 * items in a set S, each with a given size, can be added to a knapsack of
 * capacity c without exceeding the capacity and utilizing the most space
 * possible.
 */

import java.util.Random;
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
        int userChoice;

        Scanner userInput = new Scanner(System.in);
        System.out.print("Knapsack Problem - Menu:\n" +
                            "(1) Read input from file\n" +
                            "(2) Generate random input\n "+
                            "Enter choice: ");
        userChoice = userInput.nextInt();
        System.out.println();
        if (userChoice == 1)
        {
            System.out.println("Enter full patch of input file:");
            File f = new File(userInput.next());
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
            System.out.println();
            backtrackKnapSack();
            scan.close();
        }
        else if (userChoice == 2)
        {
            for (int i = 5; i <= 35; i+=5)
            {
                int[] vals = generateTestVals(i);
                n = vals.length-1;
                c = vals[0];
                S = new int[n];
                for (int x = 1; x <= n; x++)       // Populate rest of testVals with random integers
                {
                    S[x-1] = vals[x];
                }        
                System.out.println("Capacity: " + vals[0]);
                System.out.println("Number of items: " + n);
                dynamicKnapSack();
                System.out.println();
                backtrackKnapSack();
                reset();
            }
        }
        
        userInput.close();
    }

    // Method to reset global variables between multiple runs
    public static void reset()
    {
        for (int x = 0; x < n; x ++)
        {
            S[x] = 0;
            maxSubset[x] = 0;
        }
        n = 0;
        c = 0;
        maxSize = 0;
    }

    // Helper method to generate given number of random test values to populate S
    public static int[] generateTestVals(int numItems)
    {
        Random gen = new Random();

        int testVals[] = new int[numItems+1];
        testVals[0] = gen.nextInt(1000);     // Index 0 of testVals is capacity

        for (int x = 1; x <= numItems; x++)       // Populate rest of testVals with random integers
        {
            testVals[x] = gen.nextInt(1000);
        }
        // Return array of random values with index 0 being capacity
        return testVals;
    }

    //Knapsack problem solution using dynamic programming  
    public static void dynamicKnapSack()
    {
        long start = System.nanoTime();
        long end;
        boolean exist[][] = new boolean[n+1][c+1];
        boolean belong[][] = new boolean[n+1][c+1];

        // Initialize first row of exist to false for all indices other than zero
        exist[0][0] = true;
        for (int j = 1; j < c; j++)  // theta(c)
        {
            exist[0][j] = false;
        }
        
        for (int i = 1; i <= n; i++)  // theta (n)
        {
            for (int j = 0; j <= c; j++)  // theta(c)
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
        printSolution(belong, exist);  // theta(n)
        end = System.nanoTime();
        System.out.println("Time in nanoseconds: " + (end-start));
    }

    // Knapsack problem solution using backtracking
    public static void backtrackKnapSack()
    {
        maxSubset = new int[n];
        int[] subset = new int[n];
        long end;
        long start = System.nanoTime();

        // Call recursive function for backtracking
        rbacktrackKnapSack(1, subset);

        printSolution(maxSubset);
        end = System.nanoTime();
        System.out.println("Time in nanoseconds: " + (end-start) + "\n-----------");
    }

    // Recursive function for backtracking
    public static void rbacktrackKnapSack(int k, int[] subset)
    {
        if (subset.length > 0){
            for (int j = 0; j <=1; j++)
            {
                subset[k] = j;
                // if subset is full
                if (k == n-1)
                {
                    checkSubset(subset);
                }
                // if subset is not full
                else
                {
                    rbacktrackKnapSack(k+1, subset);
                }
            }
        }
    }
    
    // Helper method to check a subset to see if it is larger than the current max subset
    public static void checkSubset(int[] subset)
    {
        int[] currSubset = new int[n];
        int total = 0;

        // If value at index x is 1, add value of S at x to currSubset
        for (int x = 0; x < n; x++)
        {
            if (subset[x] == 1)
            {
                currSubset[x] = S[x];
                total += S[x];
            }
        }
        // If current total is greater than previous max and less than capacity, replace maxSize and maxSubset
        if (total > maxSize && total <= c)
        {
            maxSize = total;
            for (int x = 0; x < n; x++){ maxSubset[x] = currSubset[x]; }
        }
    }

    // Helper method to print solution for dynamic programming implementation
    public static void printSolution(boolean[][] belong, boolean[][] exists)
    {
        int total = 0;
        int i = n;
        int j = c;
        System.out.println("Dynamic Programming\n\nItems selected:");
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

    // Helper method to print solution for backtracking implementation
    public static void printSolution(int[] subset)
    {
        System.out.println("Backtracking\n\nItems selected:");
        for (int i = 0; i < subset.length; i++)
        {
            if (subset[i] > 0)
                System.out.println("Item " + (i+1) + ", Size = " + S[i] + " ");
        }
        System.out.println("Capacity: " + c + "\nTotal space used: " + maxSize);
    }
}