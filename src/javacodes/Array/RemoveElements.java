package javacodes.Array;

class RemoveElements {

    static void sortColors(int[] nums) {
        int lo = 0;
        int hi = nums.length - 1;
        int mid = 0;
        int temp;
        while (mid <= hi) {
            switch (nums[mid]) {
                case 0 -> {
                    temp = nums[lo];
                    nums[lo] = nums[mid];
                    nums[mid] = temp;
                    lo++;
                    mid++;
                }
                case 1 -> mid++;
                case 2 -> {
                    temp = nums[mid];
                    nums[mid] = nums[hi];
                    nums[hi] = temp;
                    hi--;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] nums = new int[] { 0, 1, 2, 2, 3, 0, 4, 2 };
        int val = 2;

        int pos = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val)
                nums[pos++] = nums[i];
        }

        for (int num : nums) {
            System.out.print(num + " ");
        }
        System.out.println();
        int[] arr = {2, 0, 1};
        sortColors(arr);
        for (int a: arr) {
            System.out.print(a + " ");
        }
    }
}