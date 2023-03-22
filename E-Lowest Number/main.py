import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        int min = Integer.MAX_VALUE;
        int minIndex = -1;
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
            if (a[i] < min) {
                min = a[i];
                minIndex = i;
            }
        }
        System.out.println(min + " " + (minIndex + 1));
    }
}