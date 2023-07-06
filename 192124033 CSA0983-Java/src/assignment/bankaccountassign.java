import java.util.Scanner;

public class bankaccountassign {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Account account = new Account(100.0);

        int choice;
        do {
            System.out.println("1. Deposit");
            System.out.println("2. Withdraw");
            System.out.println("3. Check Balance");
            System.out.println("4. Compute Interest");
            System.out.println("0. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter the amount to deposit: ");
                    double depositAmount = scanner.nextDouble();
                    account.deposit(depositAmount);
                    System.out.println("Amount deposited successfully.");
                    break;

                case 2:
                    System.out.print("Enter the amount to withdraw: ");
                    double withdrawAmount = scanner.nextDouble();
                    account.withdraw(withdrawAmount);
                    System.out.println("Amount withdrawn successfully.");
                    break;

                case 3:
                    System.out.println("Current balance: $" + account.getBalance());
                    break;

                case 4:
                    System.out.print("Enter the interest rate: ");
                    double interestRate = scanner.nextDouble();
                    account.computeInterest(interestRate);
                    System.out.println("Interest computed successfully.");
                    System.out.println("Current balance: $" + account.getBalance());
                    break;

                case 0:
                    System.out.println("Exiting...");
                    break;

                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }

            System.out.println(); // Print a new line for clarity
        } while (choice != 0);

        scanner.close();
    }
}
class Account {
    private double balance;

    // Constructor with initial balance parameter
    public Account(double initialBalance) {
        balance = initialBalance;
    }

    // Constructor with no initial balance (defaults to $0)
    public Account() {
        balance = 0.0;
    }

    // Function to add money to the account
    public void deposit(double amount) {
        balance += amount;
    }

    // Function to withdraw money from the account
    public void withdraw(double amount) {
        if (amount > balance) {
            System.out.println("Insufficient funds. $5 penalty charged.");
            balance -= 5.0; // Apply $5 penalty
        } else {
            balance -= amount;
        }
    }

    // Function to inquire the current balance
    public double getBalance() {
        return balance;
    }
    public double computeInterest(double interestRate) {
        double interest = balance * interestRate / 100;
        balance += interest;
        return balance;
    }
}
