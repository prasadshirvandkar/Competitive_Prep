package javacodes.Array;

public class MaxSumIncreasingSubsequence {
    public static void main(String[] args) {
        int[] arr = { 1, 101, 2, 3, 100, 4, 5 };

        int sum = arr[0];
        int currentMax = sum;
        for (int i = 1; i < arr.length; i++) {
            sum += (arr[i] > arr[i - 1]) ? arr[i] : -(Math.abs(arr[i - 1] - arr[i]));
            System.out.println(sum);
            if (sum > currentMax) {
                currentMax = sum;
            }
        }

        System.out.println(currentMax);
    }

}