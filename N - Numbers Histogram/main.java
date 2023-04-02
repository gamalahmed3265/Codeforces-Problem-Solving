import java.util.Scanner;

public class JavaApplication17 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String sy=sc.next();
        int num1=sc.nextInt();
        int array[] = new int[num1];
        for (int i = 0; i < num1; i++) {
            array[i]=sc.nextInt();
        }
        for (int i = 0; i < num1; i++) {
            
            for (int j = 0; j < array[i]; j++) {
                System.out.print(sy);
            }
            System.out.println();
        }
        
}
}
