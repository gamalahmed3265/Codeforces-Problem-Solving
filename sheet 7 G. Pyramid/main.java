package javaapplication18;

import java.util.List;
import java.util.Scanner;

public class JavaApplication18 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            System.out.print(" ".repeat(n - i));
            System.out.print("*".repeat(2 * i - 1));
            System.out.println("");
        }
    }
}
