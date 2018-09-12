package Patterns;import java.util.*;
class pattern_1
{
    public static void main()
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number of rows");
        int row=sc.nextInt();
        System.out.println("Enter the number of coloumns");
        int col=sc.nextInt();
        for(int i=1;i<=row;i++)
        {
             for(int j=1;j<=col;j++)
             {
                 System.out.print("* \t");
             }
             System.out.println();
        }
    }
}
//* * *
//* * *
//* * *