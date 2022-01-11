package javacodes.String;

class StringFrequencyConcat {
    public static void main(String[] args) {
        String s = "aaabbcccaaaaa";
        int[] freq = new int[s.length()];
        int count = 1;
        int j = 0;
        for(int i=1;i<s.length();i++) {
            if(s.charAt(i) != s.charAt(i-1) || i == s.length() - 1) {
                freq[i] = count;
                count = 1;
                j++;
            } else {
                count++;
            }
        }

        char[] newChar = new char[s.length()+j];
        for(int i=1;i<s.length();i++) {
            if(s.charAt(i) != s.charAt(i-1)) {
                newChar[i] = (char) freq[i];
                continue;
            }
            newChar[i] = s.charAt(i - 1);
        }

    }
}