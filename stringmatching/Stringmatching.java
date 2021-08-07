import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class Stringmatching {

    public static void stringmatching() {
        Scanner scan = new Scanner(System.in);
        while (scan.hasNext()) {
            String pattern = scan.nextLine();
            String text = scan.nextLine();
            containsPattern(text, pattern);
        }

        scan.close();
    }

    public static void containsPattern(String text, String pattern) {
        HashMap<Character, Integer> table = badMatchTable(pattern);
        int n = text.length() - 1;
        int m = pattern.length() - 1;

        ArrayList<String> indices = new ArrayList<>();

        int index = 0;
        while (index <= n - m) {
            if (patternMatch(text, pattern, index)) {
                indices.add("" + index);
            }

            index += table.getOrDefault(text.charAt(index + pattern.length() - 1), pattern.length());
        }

        String out = String.join(" ", indices);
        System.out.println(out);
    }


    public static HashMap<Character, Integer> badMatchTable(String pattern) {
        HashMap<Character, Integer> table = new HashMap<>();

        for (int i = 0; i < pattern.length() - 1; i++) {
            table.put(pattern.charAt(i), pattern.length() - i - 1);
        }

        return table;
    }

    public static boolean patternMatch(String text, String pattern, int index) {
        for (int i = index+pattern.length() - 1; i >= index; i--) {
            if (text.charAt(i) != pattern.charAt(i - index)) {
                return false;
            }
        }

        return true;
    }



    // Setup
    public static void main(String[] args) {
        stringmatching();
    }
}
