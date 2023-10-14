
package javaapplication18;

import java.util.Scanner;

public class JavaApplication18 {
    public static  int sum(int a,int b){
        return  a+b;
    }
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        int x=in.nextInt();
        int y=in.nextInt();
        System.out.println(sum(x, y));
    }
    
}
