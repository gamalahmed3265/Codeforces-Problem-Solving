

import java.util.Scanner;

public class Main {
    public static void summation(int a,int b){
        int sum=0;
        for (int i = a ;i <= b; i++) {
            if(i%2!=0)
                sum+=i;
        }
        System.out.println(sum);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r=sc.nextInt();
        while(r >0){
            int n=sc.nextInt();
            int m=sc.nextInt();
            
           
            if(n>m)
                summation(m,n);
            else
                summation(n,m);
            
              r--;
            }
      
}
}
