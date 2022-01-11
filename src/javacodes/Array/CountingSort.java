package javacodes.Array;

import java.util.Arrays;

public class CountingSort {
    public static void main(String[] args) {
        int a[] = {1, 4, 1, 2, 7, 5, 2};

        int count[] = new int[8];
        Arrays.fill(count, 0);

        for(int i=0;i<a.length;i++) {
            ++count[a[i]];
        }

        for(int i=1;i<count.length;i++) {
            count[i] += count[i-1];
        }

        int output[] = new int[a.length];
        for(int i=0;i<a.length;i++) {
            output[count[a[i]]-1] = a[i];
            --count[a[i]];
        }

        for(int i=0;i<output.length;i++){
            System.out.print(output[i]+" ");
        }

    }
}