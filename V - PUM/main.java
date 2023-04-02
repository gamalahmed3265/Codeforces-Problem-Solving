

import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r=sc.nextInt();
         for (int i = 1; i <= r*4; i++) {
            
             if (i%4 ==0)
                System.out.print("PUM\n");
             else
                  System.out.print(i+" ");
        }
}
}
