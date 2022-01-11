package javacodes.Numbers;

public class MissingNumberFromArray {
    public static void main(String[] args) {
        int[] nums = {9,6,4,2,3,5,7,0,1};
        int n = nums.length;
        int sum = (n * (n + 1)) / 2;
        int numSum = 0;
        for (int num : nums) {
            numSum += num;
        }

        System.out.println(sum - numSum);
    }
}
