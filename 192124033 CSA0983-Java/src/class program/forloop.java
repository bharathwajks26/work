import java.util.Scanner;
public class forloop
{
public static void main(String[] args)
{

Scanner input= new Scanner(System.in);
int n=input.nextInt();
int s=0;
for (int i=0;i<=n;i++)
{
   s=s+i;
}
System.out.println("value "+s);
}}
