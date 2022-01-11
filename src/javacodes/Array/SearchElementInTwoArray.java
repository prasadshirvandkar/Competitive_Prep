package javacodes.Array;

class SearchElementInTwoArray {

    public static void main(String[] args) {

        int a[] = {13, 17, 35, 40, 49, 55, 59};
        int b[] = {17, 35, 39, 40, 55, 58, 60};

        int j = 0;
        int count = 0;
        for(int i=0;i<a.length;i++) {
            while(j<b.length) {
                if(a[i] == b[j]) {
                    count++;
                    break;
                } else if(a[i] < b[j]) {
                    break;
                }
                j++;
            }
        }

        System.out.println(count);
    }

}