public class day2test3 {
    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
		if(i!=0){
			for(int j=0; j<i; j++){  
		     		if(j!=0){
					System.out.print(" ");
				}
				for(int k=0; k<i; k++){  
			      		System.out.print("9");
				}
			}
		System.out.println("");}
        }
    }
}
