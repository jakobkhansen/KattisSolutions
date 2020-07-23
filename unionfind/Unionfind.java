import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Unionfind {

    public static String unionfind(String[] lines) {
        int setNum = Integer.parseInt(lines[0].split(" ")[0]);
        int[] unionData = new int[setNum];
        Arrays.fill(unionData, -1);
        System.out.println(unionData[0]);

        return commandLoop(lines, unionData).trim();
    }

    public static String commandLoop(String[] commands, int[] unionData) {
        String retString = "";
        for (int i = 1; i < commands.length; i++) {
            String[] line_split = commands[i].split(" ");
            String symbol = line_split[0];

            int num1 = Integer.parseInt(line_split[1]);
            int num2 = Integer.parseInt(line_split[2]);

            if (symbol.equals("?")) {
                retString += checkUnion(unionData, num1, num2) + "\n";
            } else if (symbol.equals("=")) {
                performUnion(unionData, num1, num2);
            }
        }
        return retString;
    }

    public static int findParent(int[] unionData, int num) {
        if (unionData[num] < 0) {
            return num;
        }
        
        int current = num;
        while (unionData[current] >= 0) {
            current = unionData[current];
        }

        unionData[num] = current;
        return current;
    }

    public static void performUnion(int[] unionData, int num1, int num2) {
        int parent1 = findParent(unionData, num1);
        int parent2 = findParent(unionData, num2);

        unionData[parent1] = parent2;
    }

    public static String checkUnion(int[] unionData, int num1, int num2) {
        if (num1 == num2 || findParent(unionData, num1) == findParent(unionData, num2)) {
            return "yes";
        }

        return "no";
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

        System.out.println(unionfind(lines));

        scan.close();
    }
}
