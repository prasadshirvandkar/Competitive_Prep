package javacodes.Array;

public class NextPermutation {

    static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    static void nextPerm(int[] nums) {
        int n = nums.length;

        int mIndex = -1;
        for(int i = n - 2; i >= 0; i--) {
            if(nums[i] < nums[i+1]) {
                mIndex = i;
                int sSm = n - 1;
                while(nums[mIndex] >= nums[sSm]) {
                    sSm -= 1;
                }
                swap(nums, mIndex, sSm);
                break;
            }
        }

        // Reverse
        for (int i = mIndex + 1; i < (n + mIndex + 1) / 2; i++) {
            swap(nums, i, n + mIndex - i);
        }
    }

    public static void main(String[] args) {
        int[] arr = {1, 3, 5, 4, 2};
        nextPerm(arr);

        for(int a: arr) {
            System.out.print(a + " ");
        }
    }
}
