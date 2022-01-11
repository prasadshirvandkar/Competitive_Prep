package javacodes.Array;

import java.util.Map;
import java.util.HashMap;

public class MinDistinctElementsAfterRemoving {
    public static void main(String[] args) {
        int[] a = {3, 3, 3, 1, 2, 2};
        int m = 3;
        Map<Integer, Integer> arrMap = new HashMap<>();

        for(int i=0; i<a.length; i++) {
            arrMap.put(a[i], (arrMap.get(a[i]) != null) ? arrMap.get(a[i])+1 : 1);
        }
        
        int count = 0;
        for(Map.Entry<Integer, Integer> entry: arrMap.entrySet()) {
            if(entry.getValue() <= m) {
                m -= entry.getValue();
                count++;
            } else {
                break;
            }
        }

        System.out.println(arrMap.size() - count);
    }
}