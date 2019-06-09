import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> lines = new ArrayList<String>();
        while (sc.hasNextLine()) {
            lines.add(sc.nextLine());
        }

        ArrayList<Island> islands = create_islands(lines);
        int numSurvivors = simulateIslands(islands);
        System.out.println(numSurvivors);
    }

    public static ArrayList<Island> create_islands(ArrayList<String> lines) {
        lines.remove(0);
        ArrayList<Island> islands = new ArrayList<>();


        // Create islands
        for (int lineIndex = 0; lineIndex < lines.size(); lineIndex++) {
            String[] words = lines.get(lineIndex).split(" ");

            int threshold = Integer.parseInt(words[0]);
            boolean alive = Integer.parseInt(words[1]) != 0;
            islands.add(new Island(threshold, alive)); 
        }


        // Create pairs
        
        for (int lineIndex = 0; lineIndex < lines.size(); lineIndex++) {
            HashMap<Island, Integer> pairs = new HashMap<>();
            String[] words = lines.get(lineIndex).split(" ");


            for (int pairIndex = 2; pairIndex < words.length; pairIndex += 2) {

                int islandIndex = Integer.parseInt(words[pairIndex]) - 1;
                int amount = Integer.parseInt(words[pairIndex+1]);

                pairs.put(islands.get(islandIndex), amount); 
            }
            islands.get(lineIndex).createPairs(pairs);
        }

        return islands;
    } 

    public static int simulateIslands(ArrayList<Island> islands) {

        // Lunar cycles

        for (int i = 0; i < 3; i++) {
            for (Island island : islands) {
                for (Island pairIsland : island.getPairs().keySet()) {
                    pairIsland.sendGoods(island, island.getPairs().get(pairIsland));
                }
            }
            for (Island island : islands) {
                island.evalDeath();
            }
        }

        int deathCounter = 0;
        for (Island island : islands) {
            if (island.getAlive()) {
                deathCounter += 1;
            }
        }

        return deathCounter;
    }
}
