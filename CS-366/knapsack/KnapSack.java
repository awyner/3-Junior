public class KnapSack{
    public static void main(String[] args)
    {
        

    }

    public static void dynamicKnapSack(int[] S, int c)
    {
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
    }
}