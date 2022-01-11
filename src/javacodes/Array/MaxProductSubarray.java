package javacodes.Array;

public class MaxProductSubarray {
    public static void main(String[] args) {
        int[] a = {1, -2, -3, 0, 7, -8, -2};

        int maxSoFar = Integer.MIN_VALUE;
        int product = a[0];

        for(int i = 1; i < a.length; i++) {
            product *= a[i];
            if(product > maxSoFar) {
                maxSoFar = product;
            } else if(product == 0) {
                product = 1;
            }
        }

        System.out.println(maxSoFar);
    }
}