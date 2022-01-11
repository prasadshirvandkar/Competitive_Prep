package javacodes.Array;

public class BinarySearch {
    public static void main(String[] args) {
        int a[] = {10, 20 ,30 ,40, 50, 60};

        int data = 20;
        int low = 0, high = a.length - 1;
        int mid;

        while(low <= high) {
            mid = (low + high) / 2;
            if(a[mid] < data) {
                low = mid + 1;
            } else if(a[mid] > data) {
                high = mid - 1;
            } else {
                System.out.println("Data is Found");
                break;
            }
        }

        System.out.println("Not Found");
    }
}