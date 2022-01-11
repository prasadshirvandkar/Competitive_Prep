package javacodes.Numbers;

public class PowerExp {

    static int pow(int n, int p) {
        int res = 1;
        while(p >= 1) {
            if (p % 2 == 0) {
                n = n * n;
                p /= 2;
            } else {
                p -= 1;
                res *= n;
            }
        }

        return res;
    }

    public static void main(String[] args) {
        int n = 3, p = 3;
        System.out.println(pow(n, p));
    }
}
