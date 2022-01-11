package javacodes.Array;

import java.util.*;
public class TopKFrequentElements {
    public static void main(String[] args) {
        int[] nums = {1,1,1,2,2,3};
        int k = 2;
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, (map.get(num) != null) ? map.get(num) + 1 : 1);
        }
        
        PriorityQueue<Map.Entry<Integer, Integer>> queue = new PriorityQueue<>((x, y) -> y.getValue() - x.getValue());
        queue.addAll(map.entrySet());

        for(int i=0;i<k;i++) {
            System.out.println(Objects.requireNonNull(queue.poll()).getKey());
        }
    }
}