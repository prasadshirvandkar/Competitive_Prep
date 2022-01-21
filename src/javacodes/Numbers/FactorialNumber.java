package javacodes.Numbers;

public class FactorialNumber {

    public static void maxArea(int[] height) {
        int maxarea = 0, l = 0, r = height.length - 1;
        while (l < r) {
            maxarea = Math.max(maxarea, Math.min(height[l], height[r]) * (r - l));
            if (height[l] < height[r])
                l++;
            else
                r--;
        }
    }

    public static void main(String[] args) {
        int n = 5;
        int fact = 1;
        for(int i=1; i<=n; i++) {
            fact *= i;
        }

        System.out.println(fact);

        int[] arr = {4, 3, 1, 2, 4};
        maxArea(arr);
    }
}