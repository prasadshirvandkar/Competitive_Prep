package javacodes.Array;

import java.util.*;
public class HappyNumber {
    public static void main(String args[]) {
        int n = 1957;
        int res = 0;
        Map<Integer, Integer> map = new HashMap<>();
        
        while(n > 0) {
            res += Math.pow(n % 10, 2);
            n /= 10;
            if(n == 0) {
                if(res == 1) {
                    System.out.println(true);
                    break;
                }

                if(map.get(res) !=null && map.get(res) == 1) {
                    System.out.println(false);
                    break;
                } else {
                    map.put(res, 1);
                }
                
                n = res;
                res = 0;
            }
        }

    }
}