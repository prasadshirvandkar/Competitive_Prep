package javacodes.LinkedList;

import java.util.*;

public class PairwiseSwappingOfLinkedList { 
    Node head; 
    static class Node {
        int data; 
        Node next; 
        Node(int d) { 
            data = d; 
            next = null; 
        } 
    } 

    public void pairWiseSwap() {
        Node temp = head;

        while(temp != null && temp.next != null) {
            int k = temp.data;
            temp.data = temp.next.data;
            temp.next.data = k;
            temp = temp.next.next;
        }
    }

    public Node reverseLinkedList() {
        Node next = null;
        Node prev = null;
        Node curr = head;

        while(curr != null) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    public Node reverseLinkedListInGroups() {
        Node temp = head;
        Stack<Node> stack = new Stack<>();
        int k = 3;
        Node prev = null;

        while (temp != null) {
            int count = 0;
            while(temp != null && count < k) {
                stack.push(temp);
                temp = temp.next;
                count++;
            }

            while(!stack.isEmpty()) {
                if(prev == null) {
                    prev = stack.pop();
                    head = prev;
                } else {
                    prev.next = stack.pop();
                    prev = prev.next;
                }
            }
        }
        if (prev != null) {
            prev.next = null;
        }

        return head;
    }

    public void push(int data) {
        Node node = new Node(data);
        node.next = head; 
        head = node; 
    } 
  
    void printList() { 
        Node temp = head; 
        while (temp != null) { 
            System.out.print(temp.data + " "); 
            temp = temp.next; 
        } 
        System.out.println(); 
    } 
  
    public static void main(String args[]) { 
        PairwiseSwappingOfLinkedList llist = new PairwiseSwappingOfLinkedList(); 
        llist.push(5); 
        llist.push(4); 
        llist.push(3); 
        llist.push(2); 
        llist.push(1); 

        //Node node = llist.reverseLinkedList();
        Node node = llist.reverseLinkedListInGroups();
        while(node != null) {
            System.out.print(node.data+" ");
            node = node.next;
        }
        System.out.println();
    } 
} 