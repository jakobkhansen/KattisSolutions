import java.util.ArrayList;
import java.util.Scanner;

public class Powerstrings {

    public static void powerstrings() {
        Scanner s = new Scanner(System.in);
        String curCase = s.nextLine();
        while (curCase != null) {
            if (curCase.charAt(0) == '.') {
                return;
            }

            int currentSize = 1;
            int length = curCase.length();

            while (currentSize < length) {
                if (length % currentSize != 0) {
                    currentSize += 1;
                    continue;
                }

                boolean finished = true;

                for (int i = currentSize; i < length; i++) {
                    if (curCase.charAt(i) != curCase.charAt(i % currentSize)) {
                        finished = false;
                        break;
                    }
                }

                if (finished) {
                    System.out.println(length/currentSize);
                    break;
                }

                currentSize += 1;
            }

            if (currentSize == length) {
                System.out.println(1);
            }

            curCase = s.nextLine();
        }
    }

    // Setup
    public static void main(String[] args) {
        powerstrings();

    }
}
