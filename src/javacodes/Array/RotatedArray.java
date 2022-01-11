package javacodes.Array;

public class RotatedArray {
    public static void main(String[] args) {
        int[] arr = {4, 5, 6, 7, 1, 2, 3};
        int low = 0, high = arr.length - 1;

        int mid = -1;
        while(low <= high) {
            mid = (low + high) / 2;
            if (arr[mid] < arr[mid - 1] && arr[mid] < arr[mid + 1]) break;

            if (arr[mid] > arr[mid - 1] && arr[mid] < arr[high]) {
                high = mid;
            } else {
                low = mid;
            }
        }

        System.out.println(mid);
    }
}
