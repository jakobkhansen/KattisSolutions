import java.util.ArrayList;
import java.util.Scanner;

public class Sodaslurper {

    public static String sodaslurper(String[] lines) {
        String[] input = lines[0].split(" ");
        int emptyBottles = Integer.parseInt(input[0]);
        int bottlesFound = Integer.parseInt(input[1]);
        int bottlePrice = Integer.parseInt(input[2]);

        int current = emptyBottles + bottlesFound;

        int bought = 0;

        while (current >= bottlePrice) {
            bought++;
            current -= bottlePrice;
            current++;
        }

        return "" + bought;
    }



    // Setup
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        ArrayList<String> linesList = new ArrayList<>();

        while (scan.hasNext()) {
            linesList.add(scan.nextLine());
        }

        String[] lines = new String[linesList.size()];

        for (int i = 0; i < lines.length; i++) {
            lines[i] = linesList.get(i);
        }

        System.out.println(sodaslurper(lines));

        scan.close();
    }
}
