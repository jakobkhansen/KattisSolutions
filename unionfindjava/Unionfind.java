import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;

class Unionfind {
    static class Node {

        String label;
        int size;
        Node parent;

        public Node(String label) {
            this.label = label;
            this.parent = null;
            this.size = 0;
        }


        public Node find() {
            Node root = this;
            while (root.parent != null) {
                root = root.parent;
            }

            Node current = this;
            while (current.parent != null) {
                current.parent = root;
                current = current.parent;
            }

            return root;
        }

        public void union(Node other) {
            if (this == other) {
                return;
            }

            Node a_parent = this.find();
            Node b_parent = other.find();

            if (a_parent == b_parent) {
                return;
            }

            if (a_parent.size >= b_parent.size) {
                b_parent.parent = a_parent;
                a_parent.size += b_parent.size;
            } else {
                a_parent.parent = b_parent;
                b_parent.size += a_parent.size;
            }
        }
    }




    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();

        HashMap<String, Node> nodes = new HashMap<>();

        for (String line = br.readLine(); line != null; line = br.readLine()) {
            String[] words = line.split(" ");

            String op = words[0];
            String a = words[1];
            String b = words[2];

            if (nodes.getOrDefault(a, null) == null) {
                nodes.put(a, new Node(a));
            }

            if (nodes.getOrDefault(b, null) == null) {
                nodes.put(b, new Node(b));
            }

            Node a_node = nodes.get(a);
            Node b_node = nodes.get(b);

            if (op.equals("?")) {
                String result = (a_node.find() == b_node.find()) ? "yes" : "no";
                System.out.println(result);
            } else {
                a_node.union(b_node);
            }
        }
    }
}
