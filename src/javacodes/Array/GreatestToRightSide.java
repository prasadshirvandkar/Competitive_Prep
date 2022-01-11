package javacodes.Array;

import java.util.Arrays;

public class GreatestToRightSide {
    public static void main(String[] args) {
        int[] arr = new int[] { 17, 18, 5, 4, 6, 1 };
        int n = arr.length;

        int i = n - 1;
        int j = n - 2;

        while (j > 1) {
            if (arr[i] > arr[j]) {
                arr[j] = arr[i];
                j--;
            } else {
                i = j;
            }
        }

        System.out.println("List: " + Arrays.toString(arr));
    }
}