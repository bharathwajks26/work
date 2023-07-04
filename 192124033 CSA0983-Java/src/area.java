import java.io.*;
import java.util.Scanner;
public class area
{
public static void main(String[] args)
{

Scanner input = new Scanner(System.in);
 x =input.next();
 y =input.next();
y=y/100;
 a=x*y;
 c=2*(x+y);
System.out.println("area "+a);
System.out.println("circumference "+c);
}
}
