package javaapplication18;

import java.util.List;
import java.util.Scanner;
import java.util.Arrays;

public class JavaApplication18 {

    public static String can_form_triangle(int[] segments) {
        Arrays.sort(segments);
        for (int i = 0; i < segments.length - 2; i++) {
            if (segments[i] + segments[i + 1] > segments[i + 1]) {
                return "YES";
            }
        }
        return "NO";
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        sc.close();
        System.out.println(can_form_triangle(arr));
    }
}
