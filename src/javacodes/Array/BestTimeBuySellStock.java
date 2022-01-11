package javacodes.Array;

public class BestTimeBuySellStock {

    static int bestTimeToBuySellStock(int[] prices) {
        if(prices.length == 1) return 0;

        int buy = prices[0], best = 0;
        for (int i = 1; i < prices.length; i++) {
            if(prices[i] < buy) {
                buy = prices[i];
            } else {
                best = Math.max(prices[i] - buy, best);
            }
        }

        return best;
    }

    public static void main(String[] args) {
        int[] nums = {3,2,1};
        System.out.println(bestTimeToBuySellStock(nums));
    }
}
