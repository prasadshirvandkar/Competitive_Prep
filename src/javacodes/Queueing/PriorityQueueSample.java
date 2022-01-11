package javacodes.Queueing;

import java.util.*;

public class PriorityQueueSample {

    public static void main(String[] args) {
        PriorityQueue<Integer> pr = new PriorityQueue<>((x, y) -> y-x);
        pr.add(90);
        pr.add(12);
        pr.add(44);
        pr.add(1);

        System.out.println(pr.peek());
        System.out.println(pr.poll());
        System.out.println(pr.peek());

    }

}