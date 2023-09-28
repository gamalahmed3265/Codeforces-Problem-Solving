import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String S = scanner.nextLine().trim();

        // Function to check if "hello" is a subsequence of S
        String result = findHelloSubsequence(S);

        System.out.println(result);
    }

    public static String findHelloSubsequence(String s) {
        String target = "hello";
        int i = 0;  // Index for the target string "hello"

        for (char c : s.toCharArray()) {
            if (c == target.charAt(i)) {
                i++;
                if (i == target.length()) {
                    return "YES";
                }
            }
        }

        return "NO";
    }
}
