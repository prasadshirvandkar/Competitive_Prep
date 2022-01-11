package javacodes.Array;

public class BitonicArrayIdentification {
    public static void main(String[] args) {
        int a[] = {10, 20, 30, 40};
        int trend = 0;
        int len = a.length;

        for(int i=0;i<len-1;i++) {
            if(a[i] < a[i+1]) {
                if(trend == -1) {
                    trend = 4;
                    break;
                } 
                trend = 1;
            } else if(a[i] > a[i+1]) {
                if(trend == 1) {
                    trend = 3;
                    break; 
                }
                trend = -1;
            }
        }

        System.out.println(trend);
    }
}