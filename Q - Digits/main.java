

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num1=sc.nextInt();
        int array[] = new int[num1];
        for (int i = 0; i < num1; i++) {
            array[i]=sc.nextInt();
        }
        for (int i = 0; i < num1; i++) {
            String re=String.valueOf(array[i]);
            for (int j = re.length()-1; j >=0; j--) {
                System.out.print(re.charAt(j)+" ");
            }
            System.out.println();
        }
}
}
