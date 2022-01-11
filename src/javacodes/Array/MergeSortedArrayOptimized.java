package javacodes.Array;

public class MergeSortedArrayOptimized {
    public static void main(String[] args) {
        int[] nums1 = new int[] { 1, 2, 3, 0, 0, 0 };
        int[] nums2 = new int[] { 2, 5, 6 };
        int m = 3, n = 3;
        int t = m + n;

        for (int i = t - 1; i >= 0; i--) {
            if (n == 0)
                break;

            if (m == 0) {
                nums1[i] = nums2[n - 1];
                n--;
                continue;
            }

            if (nums2[n - 1] > nums1[m - 1]) {
                nums1[i] = nums2[n - 1];
                n--;
            } else if (nums2[n - 1] == nums1[m - 1]) {
                nums1[i] = nums1[m - 1];
                i--;
                m--;
                nums1[i] = nums2[n - 1];
                n--;
            } else {
                nums1[i] = nums1[m - 1];
                m--;
            }
        }

        for (int a : nums1) {
            System.out.print(a + " ");
        }
    }
}
