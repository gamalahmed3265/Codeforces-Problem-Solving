package javaapplication17;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num1=sc.nextInt(); int num2=sc.nextInt(),count=-1;
        
        for (int i = num1; i <= num2; i++) {
            int x=i;
            int luckly=0;
            while (x>0) {                
                if(x%10!=4 && x%10!=7)
                 luckly++;
                x/=10;
            }
            if (luckly==0){
                 System.out.print(i+" ");
                count++;
            }               
        }
        if(count==-1)
            System.out.println(-1);
}
}