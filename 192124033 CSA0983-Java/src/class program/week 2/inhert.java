import java.util.*;
class inhert {
  public static void main(String[] args) {
	c2 obj= new c2();
	obj.display();
	obj.display1();
  }
}
class c1 {

	int x=10;
	public void display(){    
	System.out.println(x);}

  }
class c2 extends c1{

	int y=5;
	public void display1(){    
	System.out.println(y);}
  
}

