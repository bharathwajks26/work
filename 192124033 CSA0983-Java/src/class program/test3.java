import java.util.Scanner;

public class test3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the annual income: ");
        double income = scanner.nextDouble();

        double deduction = 0.0;

        if (income <= 500000) {
            deduction = 0.0;
        } else if (income <= 750000) {
            deduction = (income - 500000) * 0.05;
        } else if (income <= 1000000) {
            deduction = 25000 + (income - 750000) * 0.10;
        } else if (income <= 1500000) {
            deduction = 75000 + (income - 1000000) * 0.12;
        } else {
            deduction = 125000 + (income - 1500000) * 0.20;
        }

        System.out.println("Tax Deduction: " + deduction);

        scanner.close();
    }
}
