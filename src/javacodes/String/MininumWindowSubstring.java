package javacodes.String;

class MinimumWindowSubstring {
    private static int NO_OF_CHARS = 256;

    public static void main(String[] args) {
        String str = "this is a test string";
        String pattern = "tist";

        int strFreq[] = new int[NO_OF_CHARS];
        int patFreq[] = new int[NO_OF_CHARS];
        int count = 0;
        int start = 0, actualStart = -1, minLength = Integer.MAX_VALUE;

        for (int i = 0; i < pattern.length(); i++) {
            patFreq[pattern.charAt(i)]++;
        }

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            strFreq[c]++;

            if (strFreq[c] <= patFreq[c])
                count++;

            if (count == pattern.length()) {
                while (strFreq[str.charAt(start)] > patFreq[str.charAt(start)] || patFreq[str.charAt(start)] == 0) {
                    if (strFreq[str.charAt(start)] > patFreq[str.charAt(start)]) {
                        strFreq[str.charAt(start)]--;
                    }
                    start++;
                }

                minLength = Math.min(minLength, i - start + 1);
                actualStart = start;
            }
        }

        System.out.println(str.substring(actualStart, actualStart + minLength));
    }
}

/*
 * "this is a test string" "tist" t = 2, i = 1, s = 1 =========================
 */