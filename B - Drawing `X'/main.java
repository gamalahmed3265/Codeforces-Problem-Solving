

import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r=sc.nextInt();
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < r; j++) {
             if(i == j && i != r/2 && j != r/2)
                    System.out.print("\\");
             else if (i == r/2 && j == r/2)
                    System.out.print("X");
             else if(j != r/2 && i == ((r-1)-j))
                    System.out.print("/");
            else 
                    System.out.print("*");
            
        }
            System.out.println();
        }
         
         
}
}
