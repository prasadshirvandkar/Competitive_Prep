package javacodes.Array;

class MaxProfitBuySell {

    static int maxProfitBuySell(int[] nums) {
        int buy = 0;
        int sell = 0;
        int sum = 0;
        int n = nums.length;

        for(int i=0;i<n-1;i++) {
            if(nums[i] > buy && nums[i+1] < nums[i] && buy != 0) {
                sum += Math.abs(buy - nums[i]);
                buy = 0;
                sell = 0;
            } else if((buy == 0 && sell == 0) || buy > nums[i]) {
                buy = nums[i];
                sell = 1;
            }
        }

        if(sell == 1 && buy < nums[n - 1]) sum += Math.abs(buy - nums[n - 1]);

        return sum;
    }

    public static void main(String[] args) {
        int a[] = {7,1,5,3,6,4};
        int sum = maxProfitBuySell(a);
        System.out.println(sum);
    }
}