import java.util.Scanner;
public class area
{
public static void main(String[] args)
{

Scanner input = new Scanner(System.in);
int x =input.nextInt();
int y =input.nextInt();
y=y/100;
int a=x*y;
int c=2*(x+y);
System.out.println("area "+a);
System.out.println("circumference "+c);
}
}
