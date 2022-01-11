package javacodes.Tree;

public class BinarySearchTree {

    class Node {
        int key;
        Node left, right;

        public Node(int item) {
            key = item;
            left = right = null;
        }
    }

    Node root;

    BinarySearchTree() {
        root = null;
    }

    void insert(int key) {
        root = insertRec(root, key);
    }

    Node insertRec(Node root, int key) {
        if (root == null) {
            root = new Node(key);
            return root;
        }

        if (key < root.key)
            root.left = insertRec(root.left, key);
        else if (key > root.key)
            root.right = insertRec(root.right, key);

        return root;
    }

    void closestNode(double target) {
        if (root == null)
            System.out.println("Node Null");
        int closest = root.key;

        while (root != null) {
            if (Math.abs(root.key - target) <= Math.abs(closest - target)) {
                closest = root.key;
            }

            if (root.key > target) {
                root = root.left;
            } else {
                root = root.right;
            }
        }

        System.out.println(closest);
    }

    void inorder() {
        inorderRec(root);
    }

    void inorderRec(Node root) {
        if (root != null) {
            inorderRec(root.left);
            System.out.println(root.key);
            inorderRec(root.right);
        }
    }

    public static void main(String[] args) {
        BinarySearchTree tree = new BinarySearchTree();

        tree.insert(5);
        tree.insert(4);
        tree.insert(9);
        tree.insert(2);
        tree.insert(8);
        tree.insert(10);

        // tree.inorder();
        tree.closestNode(6.124780);
    }
}