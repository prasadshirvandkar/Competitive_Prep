package javacodes.Array;

import java.util.ArrayList;
import java.util.List;

public class DuplicateArrays {

    static List<Integer> findDuplicates(int[] nums) {
        List<Integer> result = new ArrayList<>();

        for (int i = 0;i<nums.length;i++){
            int idx = Math.abs(nums[i])-1; // since num[i] could be negative we need to abs the hell out of it!
            if (nums[idx] > 0){
                nums[idx] = - nums[idx]; // we mark i as seen once
            }else{
                result.add(idx+1); // we have a dup!
            }
        }
        return result;
    }

    static void duplicateInArray() {
        int[] numRay = {4, 3, 2, 7, 8, 2, 3, 1};
   
        for (int i = 0; i < numRay.length; i++) {
            numRay[numRay[i] %  numRay.length] = numRay[numRay[i] %  numRay.length] + numRay.length;
        } 
        System.out.println("The repeating elements are : "); 
        for (int i = 0; i < numRay.length; i++) { 
            if (numRay[i] >= numRay.length*2) { 
                System.out.println(i + " ");
            } 
        } 
    }

    public static void main(String[] args) {
        // duplicateInArray();
        int[] nums = {4, 3, 2, 7, 8, 2, 3, 1};
        findDuplicates(nums);
    }
}