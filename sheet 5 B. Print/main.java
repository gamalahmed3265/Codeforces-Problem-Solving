

import java.util.Scanner;

public class JavaApplication18 {
    public static  void print(int a){
        for (int i = 1; i <= a; i++) {
            if (i!=a) {
                System.out.print(i+" ");
            }else{
                System.out.print(i);
            }
        }
    }
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        int x=in.nextInt();
        print(x);
    }
    
}
