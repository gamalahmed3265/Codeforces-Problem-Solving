import java.util.Scanner;

public class WonderfulNumber {
    // Function to check if a number is odd
    public static boolean isOdd(int N) {
        return N % 2 == 1;
    }

    // Function to check if a binary representation is a palindrome
    public static boolean isPalindromeBinary(int N) {
        String binaryStr = Integer.toBinaryString(N);
        int left = 0;
        int right = binaryStr.length() - 1;

        while (left < right) {
            if (binaryStr.charAt(left) != binaryStr.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();

            if (isOdd(N) && isPalindromeBinary(N)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
     
    }
}
