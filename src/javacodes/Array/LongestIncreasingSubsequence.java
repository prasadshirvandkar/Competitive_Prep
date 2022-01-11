package javacodes.Array;

public class LongestIncreasingSubsequence {
    public static void main(String args[]) {
        int arr[] = {10, 22, 9, 33, 21, 50, 41, 50, 60};

        int cache[] = new int[arr.length]; 
        for(int i=0;i<arr.length;i++) {
            cache[i] = 1;
        }

        for(int i=1;i<arr.length;i++) {
            for(int j=0;j<i;j++) {
                if(arr[i] > arr[j]) {
                    cache[i] = Math.max(cache[i], cache[j] + 1);
                }
            } 
        }

        for(int i=0;i<cache.length;i++) {
            System.out.print(cache[i]+" ");
        }
    }
}