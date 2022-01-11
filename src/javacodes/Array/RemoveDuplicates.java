package javacodes.Array;

public class RemoveDuplicates {
    public static void main(String[] args) {
        int[] nums = {0, 0, 1, 6, 6, 9, 10, 10, 16, 16, 16, 16, 20};
        
        int count = 1;
        for(int i=1;i<nums.length;i++) {
            if(nums[i] != nums[i-1]) {
                count++;
                nums[count-1] = nums[i];
            } 
        }

        for(int i=0;i<count;i++) {
            System.out.print(nums[i] + " ");
        }
    }
}