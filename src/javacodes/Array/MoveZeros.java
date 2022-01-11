package javacodes.Array;

public class MoveZeros {
    public static void main(String[] args) {
        int nums[] = { 0, 1, 0, 3, 12 };
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[count++] = nums[i];
            }
        }

        for (int i = count; i < nums.length; i++) {
            nums[count++] = 0;
        }
        for (int i = 0; i < nums.length; i++) {
            System.out.print(nums[i] + " ");
        }
    }
}
