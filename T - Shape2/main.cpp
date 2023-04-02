

import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r=sc.nextInt();
        int space=r-1;
         for (int i = 1; i <= r; i++) {
              for (int j = 1; j <= space; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j < i*2; j++) {
                System.out.print("*");
            }
            space--;
            System.out.println();
        }
}
}
