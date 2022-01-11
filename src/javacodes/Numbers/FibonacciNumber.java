package javacodes.Numbers;

public class FibonacciNumber {
    static int getFibonnacci(int n) {
        if (n == 1) return 1;

        int res = 0;
        int a = 0;
        int b = 1;

        for(int i=0; i<n-1; i++) {
            res = a + b;
            a = b;
            b = res;
        }

        return res;
    }

    public static void main(String[] args) {
        System.out.println(getFibonnacci(1));
    }
}