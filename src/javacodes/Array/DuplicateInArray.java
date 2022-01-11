package javacodes.Array;

public class DuplicateInArray {
    public static void main(String[] args) {
        int[] arr = {3, 1, 3, 4, 2};

        int slow = arr[0], fast = arr[0];
        do {
            slow = arr[slow];
            fast = arr[arr[fast]];
        } while (slow != fast);

        fast = arr[0];
        while(fast != slow) {
            fast = arr[fast];
            slow = arr[slow];
        }

        System.out.println(slow);
    }
}
