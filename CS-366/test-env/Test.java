public class Test
{
    public static boolean[] used;
    public static void main(String[] args)
    {
        int n = 10;
        int[] s = new int[n];
        used = new boolean[n];

        for (int i=0;i<n;i++)
        {
            used[i] = false;
        }
        rsubsets(s, 0, n);
    }

    public static void rsubsets(int[] s, int k, int n)
    {
        if (s[0] == 0)
        {
            System.out.println("{ }");
        }
        for (int j=1;j<=n;j++)
        {
            s[k] = j;
            /*for (boolean x : used)
            {
                System.out.print(x + " ");
            }
            System.out.println();*/
            if (!used[j-1])
            {
                used[j-1] = true;
                System.out.print("{ ");
                for (int i : s)
                {
                    System.out.print(i + " ");
                }
                System.out.println("}");
            }
            if (k == n-1)
            {
                System.out.println("Done");
            }
            else
            {    
                rsubsets(s, k+1, n);
            }
            
        }
        for (int x=0;x<n;x++){
            used[x] = false;
        }
    }
}