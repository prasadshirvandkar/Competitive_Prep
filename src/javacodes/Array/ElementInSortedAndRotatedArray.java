package javacodes.Array;

public class ElementInSortedAndRotatedArray {
    public static void main(String[] args) {
        int[] a = {5, 6, 7, 8, 9, 1, 2, 3, 4};
        int low = 0, high = a.length - 1;
        while(low < high) {
            int mid = low + (high - low) / 2;

            if(a[mid] == a[high]) high--;
            else if(a[mid] > a[high]) low = mid + 1;
            else high = mid;
        }

        System.out.println(a[high]);
    }
}