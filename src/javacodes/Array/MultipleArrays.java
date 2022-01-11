package javacodes.Array;

import java.util.Map;
import java.util.HashMap;

public class MultipleArrays {
    public static void main(String[] args) {
        int[] a = { 1, 2, 3 };
        int[] b = { 9, 2, 2, 3 };
        int[] c = { 6, 2, 3, 3 };
        int[] d = { 1, 1, 1 };
        int arrayCount = 3;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < b.length; i++) {
            map.put(b[i], map.get(b[i]) != null ? map.get(b[i]) + 1 : 1);
        }

        for (int i = 0; i < c.length; i++) {
            map.put(c[i], map.get(c[i]) != null ? map.get(c[i]) + 1 : 1);
        }

        for (int i = 0; i < d.length; i++) {
            map.put(d[i], map.get(d[i]) != null ? map.get(d[i]) + 1 : 1);
        }

        boolean validArray = true;
        for (int i = 0; i < a.length; i++) {
            if (map.get(a[i]) != arrayCount) {
                validArray = false;
                break;
            }
        }

        System.out.println(validArray);
    }

}