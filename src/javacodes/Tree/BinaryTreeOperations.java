package javacodes.Tree;

import java.util.Queue;
import java.util.LinkedList;
import java.util.Stack;

public class BinaryTreeOperations { 

    static int height = 0;

    Node root; 
    static class Node { 
        int data; 
        Node left, right; 
        Node(int data) { 
            this.data = data; 
            this.left = null; 
            this.right = null; 
        } 
    } 

    public Node insertLevelOrder(int[] arr, Node root) { 
        Queue<Node> nodeQ = new LinkedList<>();
        int count = 0;
        while(count < arr.length) {
            Node curr = nodeQ.poll();
            if(count == 0) {
                Node newNode = new Node(arr[count]);
                root = newNode;
                curr = root;
                count++;
            }
            
            if(curr.left == null) {
                Node leftNode = new Node(arr[count]);
                curr.left = leftNode;
                nodeQ.add(leftNode);
                count++;
            }

            if(curr.right == null && count < arr.length - 1) {
                Node rightNode = new Node(arr[count]);
                curr.right = rightNode;
                nodeQ.add(rightNode);
                count++;
            } 
        }

        return root; 
    } 

    public void printInSpiralForm(Node root) {
        System.out.print("Spiral Traversal: ");
        if(root == null) return;

        Stack<Node> s1 = new Stack<>();
        Stack<Node> s2 = new Stack<>();
        s1.push(root);

        while(!s1.isEmpty() || !s2.isEmpty()) {            
            while(!s1.isEmpty()) {
                Node node = s1.pop();
                System.out.print(node.data+" ");
                
                if(node.left != null) {
                    s2.push(node.left);
                }

                if(node.right != null) {
                    s2.push(node.right);
                }
            }

            while(!s2.isEmpty()) {
                Node node = s2.pop();
                System.out.print(node.data+" ");

                if(node.right != null) {
                    s1.push(node.right);
                }

                if(node.left != null) {
                    s1.push(node.left);
                }
            }
        }
    }

    public void levelOrderTraversal(Node root) {
        System.out.print("Level Order Traversal: ");
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);
        while(true) {
            int currSize = queue.size();
            if(currSize == 0) {
                return;
            }
            height++;

            while(currSize-- > 0) {
                Node node = queue.poll();
                System.out.print(node.data+" ");

                if(node.left != null) queue.add(node.left);
                if(node.right != null) queue.add(node.right);            
            }
        }
    }

    public void mirror(Node root) {
        if(root == null) return;

        Queue<Node> queue = new LinkedList<>();
        queue.add(root);

        while(!queue.isEmpty()) {
            Node node = queue.poll();

            Node temp = node.left;
            node.left = node.right;
            node.right = temp;

            if(node.left != null) {
                queue.add(node.left);
            }

            if(node.right != null) {
                queue.add(node.right);
            }
        }
    
    }

    public void inOrder(Node root) { 
        if (root != null) { 
            inOrder(root.left); 
            System.out.print(root.data + " "); 
            inOrder(root.right); 
        } 
    } 
  
    public static void main(String args[]) { 
        BinaryTreeOperations tree = new BinaryTreeOperations();
        int arr[] = { 1, 2, 3, 4, 5, 6, 7, 8 }; 
        tree.root = tree.insertLevelOrder(arr, tree.root); 
        System.out.print("Inorder Traversal: ");
        tree.inOrder(tree.root); 
        System.out.println();
        tree.printInSpiralForm(tree.root);
        System.out.println();
        tree.levelOrderTraversal(tree.root);
        System.out.println("\nHeight: "+height);
        tree.mirror(tree.root);
        System.out.println("Mirrored java.Tree:");
        tree.levelOrderTraversal(tree.root);
    } 
} 