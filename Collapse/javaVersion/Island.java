import java.util.HashMap;

public class Island {
    private int threshold;
    private boolean alive;
    private int current;
    private HashMap<Island, Integer> pairs = new HashMap<>();

    public Island(int threshold, boolean alive) {
        this.threshold = threshold;
        this.alive = alive;
        this.current = 0;
        this.pairs = null;
    }

    public void sendGoods(Island island, int amount) {
        if (alive) {
            island.receiveGoods(amount);
        }
    }

    private void receiveGoods(int amount) {
        if (alive) {
            this.current += amount;
        }
    }

    public boolean getAlive() {
        return alive;
    }

    public void evalDeath() {
        if (current < threshold) {
            alive = false;
        }
        current = 0;
    }

    public void createPairs(HashMap<Island, Integer> createdPairs) {
        pairs = createdPairs;
    }

    public HashMap<Island, Integer> getPairs() {
        return pairs;
    }
}
