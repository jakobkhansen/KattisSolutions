import java.io.BufferedReader; 
import java.io.IOException; 
import java.io.InputStreamReader; 
import java.util.Scanner; 
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.ArrayDeque;
import java.io.PrintWriter;

public class Teque {

    static class WeirdDeque {
        int start;
        int end;
        int size = 0;
        int[] array;
        public WeirdDeque() {
            array = new int[1000000];
            start = array.length / 2;
            end = array.length / 2;
        }

        public void addFirst(int value) {
            if (start == end) {
                end++;
            }
            //System.out.println("Pushing " + value + " to front at index " + start);
            array[start] = value;
            start--;
            size++;
        }

        public void addLast(int value) {
            if (start == end) {
                start--;
            }
            array[end] = value;
            end++;
            //System.out.println("Pushing " + value + " to back at index " + end);
            size++;
        }

        public int removeFirst() {
            int temp = array[start + 1];
            start++;
            size--;

            return temp;
        }

        public int removeLast() {
            int temp = array[end - 1];
            end--;
            size--;

            return temp;
        }

        public int get(int index) {
            //System.out.println("OG index " + index);
            int x = start + 1 + index;
            //System.out.println("Getting index " + x);
            return array[x];
        }

        public int size() {
            return size;
        }
    }

    static WeirdDeque left, right;


    public static void rearrange() {
        // Left much larger
        if (left.size() - right.size() >= 2) {
            right.addFirst(left.removeLast());

        // Right much larger
        } else if (right.size() - left.size() >= 2) {
            left.addLast(right.removeFirst());
        }
    }


    // Setup
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
        PrintWriter out = new PrintWriter(System.out);
        int N = Integer.parseInt(br.readLine());

        left = new WeirdDeque();
        right = new WeirdDeque();

        
        for (int i = 0; i < N; i++) {
            String[] line = br.readLine().split(" ");
            String command = line[0];
            int number = Integer.parseInt(line[1]);
            char first = command.charAt(0);
            switch (command) {
                case "push_back":
                    right.addLast(number);
                    rearrange();
                    break;
                case "push_front":
                        left.addFirst(number);
                        rearrange();
                        break;

                case "push_middle":
                    if (left.size() >= right.size()) {
                        left.addLast(number);
                    } else {
                        left.addLast(right.removeFirst());
                        right.addFirst(number);
                    }

                    rearrange();
                    break;
                case "get":
                    if (number < left.size()) {
                        out.write(left.get(number) + "\n");
                    } else {
                        out.write(right.get(number - left.size()) + "\n");
                    }
                    break;
            }
            out.flush();

        }
    }
}
