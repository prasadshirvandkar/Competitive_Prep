package javacodes.Array;

public class PlusOne {

    static int[] plusOne(int[] digits) {
        boolean carry = false;
        for(int i = digits.length - 1; i >= 0; i--) {
            if(digits[i] == 9) {
                digits[i] = 0;
                if (i == 0) carry = true;
            } else {
                digits[i] += 1;
                break;
            }
        }

        if (carry) {
            int[] plusOne = new int[digits.length + 1];
            plusOne[0] = 1;
            System.arraycopy(digits, 0, plusOne, 1, digits.length);
            return plusOne;
        }

        return digits;
    }

    public static void main(String[] args) {
        int[] nums = {1, 0, 2, 4};
        int[] plusOneArr = plusOne(nums);
        for (int p: plusOneArr) {
            System.out.print(p + " ");
        }
    }
}
