package javacodes.Array;

public class RotateArray {
    static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    static void rotate(int[] nums, int k) {
        if(nums.length == 1) return;

        int n = nums.length;
        k %= n;
        int nk = n - k;

        for(int i = 0; i < nk / 2; i++) {
            swap(nums, i, nk - i - 1);
        }

        for(int i = nk; i < (n + nk) / 2; i++) {
            swap(nums, i, n + nk - i - 1);
        }

        for(int i = 0; i < n / 2; i++) {
            swap(nums, i, n - i - 1);
        }
    }

    public static void main(String[] args) {
        for(int k = 0; k <= 4; k++) {
            int[] nums = {-1, -100, 3, 99};
            rotate(nums, k);
            System.out.println("Rotation for K = " + k);
            for (int n : nums) {
                System.out.print(n + " ");
            }
            System.out.println();
        }

        int[] nums = {7, 91, 1, 6, 1, 6, 1, 3, 8, 9, 1};
        rotate(nums, 12);
        for (int n : nums) {
            System.out.print(n + " ");
        }
    }
}