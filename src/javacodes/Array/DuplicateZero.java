package javacodes.Array;

class DuplicateZero {
    public static void main(String[] args) {
        int[] arr = new int[] { 2, 4, 0, 5, 6, 0, 1, 2 };
        int n = arr.length - 1;
        int possibleDups = 0;

        for (int i = 0; i <= n; i++) {
            if (arr[i] == 0) {
                if (i == n - possibleDups) {
                    arr[n] = 0;
                    n--;
                    break;
                }
                possibleDups++;
            }
        }

        System.out.println(n);

        for (int i = n - possibleDups; i > 0; i--) {
            if (arr[i] == 0) {
                arr[i + possibleDups] = arr[i];
                possibleDups--;
                arr[i + possibleDups] = 0;
            } else {
                arr[i + possibleDups] = arr[i];
            }
        }

        for (int j : arr) {
            System.out.print(j + " ");
        }
    }
}