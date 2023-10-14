
package javaapplication18;

import java.util.List;
import java.util.Scanner;

public class JavaApplication18 {
    public static void swappingMatrix(int[][] matrix,int N, int X, int Y) {
        int[] tem = matrix[X - 1];
        matrix[X - 1] = matrix[Y - 1];
        matrix[Y - 1] = tem;
        for (int i = 0; i < N; i++) {
            int temY=matrix[i][X-1];
            matrix[i][X-1]=matrix[i][Y-1];
            matrix[i][Y-1]=temY;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input: Read N, the number of elements
        int N = scanner.nextInt();
        int X = scanner.nextInt();
        int Y = scanner.nextInt();

        int[][] matrix = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                matrix[i][j] = scanner.nextInt();
            }
        }
        swappingMatrix(matrix,N ,X, Y);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println("");
        }
        scanner.close();
    }
}
