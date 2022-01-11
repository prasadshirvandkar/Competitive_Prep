package javacodes.Array;

import java.util.*;
public class BalancingArray {
    private static int run(List<Integer> nums) {
        int odd = 0,even=0;
        for(int i=0;i<nums.size();i++){
            if(i%2==0)
                even+=nums.get(i);
            else
                odd+=nums.get(i);
        }
        int ans = 0;
        int prevOdd = 0,prevEven = 0;
        for(int i=0;i<nums.size();i++){
            int x = even - prevEven;
            int y = odd - prevOdd;
            if(i%2==0)
                x-=nums.get(i);
            else
                y-=nums.get(i);
            if(prevOdd + x == prevEven + y)
                ans++;
            if(i%2==0)
                prevEven+=nums.get(i);
            else
                prevOdd+=nums.get(i);
        }
        return ans;
    }
    
    public static void main(String args[]) {
        List<Integer> list = new ArrayList<>();
        list.add(2);
        list.add(1);
        list.add(6);
        list.add(4);

        System.out.println(run(list));
    }
}