package javacodes.Array;

public class MergeSortedArrays {
    public static void main(String[] args) {
        int[] nums1 = new int[] { 1, 2, 3, 0, 0, 0 };
        int[] nums2 = new int[] { 2, 5, 6 };
        int m = 3, n = 3;

        int t = m + n;
        int c = t - 1;

        for (int k = t - (1 + n); k >= 0; k--) {
            nums1[c--] = nums1[k];
        }

        for (int k = 0; k < n; k++) {
            nums1[k] = 0;
        }

        int i = n;
        int j = 0;
        c = 0;
        while (i < t && j < n) {
            if (nums1[i] < nums2[j]) {
                nums1[c++] = nums1[i++];
            } else if (nums1[i] == nums2[j]) {
                nums1[c++] = nums1[i++];
                nums1[c++] = nums2[j++];
            } else {
                nums1[c++] = nums2[j++];
            }
        }

        for (int k = j; k < n; k++) {
            nums1[c++] = nums2[k];
        }

        for (int a : nums1) {
            System.out.print(a + " ");
        }
    }
}
