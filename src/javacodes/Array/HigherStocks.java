package javacodes.Array;

import java.util.ArrayList;
import java.util.List;

//Find Groups of Increasing Subsequence
public class HigherStocks {
    public static void main(String[] args) {
        List<Integer> stocks = new ArrayList<>() {
            {
                add(3);
                add(4);
                add(5);
                add(3);
                add(5);
                add(7);
                add(8);
            }
        };
        int k = 3;
        int count = 0, i = 1, j = 0;

        while (i < stocks.size()) {
            if (stocks.get(i) > stocks.get(i - 1)) {
                j = i;
                int c = 1;
                while (j < stocks.size() && stocks.get(j) > stocks.get(j - 1) && c < 3) {
                    c++;
                    j++;
                }

                if (c == k) {
                    count++;
                }
            }
            i++;
        }

        System.out.println(count);
    }
}
