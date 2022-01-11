package javacodes.Array;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class SumPairs {
    public static void main(String[] args) {
        int[] arr = new int[] { 5, 7, 9, 13, 11, 6, 6, 3, 3 };
        int sum = 12;

        Set<Integer> diffSet = new HashSet<>();
        Map<Integer, Integer> diffMap = new HashMap<>();
        int num = 0;
        int sumPairCount = 0;

        for (int i = 0; i < arr.length; i++) {
            num = sum - arr[i];
            if (diffSet.contains(num)) {
                sumPairCount++;
                diffSet.remove(num);
                diffMap.put(arr[i], num);
            } else {
                diffSet.add(arr[i]);
            }
        }

        System.out.println("\n" + sumPairCount);
        diffMap.forEach((key, value) -> {
            System.out.println("(" + key + ", " + value + ")");
        });
    }
}