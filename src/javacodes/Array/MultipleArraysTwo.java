package javacodes.Array;

import java.util.Map;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class MultipleArraysTwo {
    static Map<Integer, List<Integer>> map = new HashMap<>();

    private static void mapOps(int[] array, int p) {
        for(int i=0;i<array.length;i++) {
            List<Integer> list = null;
            if(map.get(array[i]) != null) {
                list = map.get(array[i]);
                list.add(p);
                map.put(array[i], list);
            } else {
                list = new ArrayList<>();
                list.add(p);
                map.put(array[i], list);
            }
        }
    }

    public static void main(String[] args) {
        int[] a = {1, 2, 3};
        int[] b = {9, 2, 2, 3};
        int[] c = {6, 2, 3, 3};
        int[] d = {1, 1, 1};
        int arrayCount = 3;
        
        mapOps(b, 1);
        mapOps(c, 2);
        mapOps(d, 3);

        boolean validArray = true;
        int maxCount = 0;
        int validItem[] = new int[a.length];
        int index = 0;
        for(int i=0;i<a.length;i++) {
            int count = map.get(a[i]).size();
            if(map.get(a[i]).size() != arrayCount) {
                validArray = false;
            }
            if(count > maxCount) {
                maxCount = count;
                index = 0;
                validItem[index++] = i;
            } else if(count == maxCount) {
                validItem[index++] = i;
            }
        }

        for(int i=0;i<validItem.length;i++) {
            System.out.println(validItem[i]);
        }

        System.out.println(validArray);
    }
    
}