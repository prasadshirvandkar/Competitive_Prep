package javacodes.String;

public class LongestCommonPrefix {

    private static int getMinLength(String[] strs) {
        int minLength = strs[0].length();
        for(String s: strs) {
            if(s.length() < minLength) minLength = s.length(); 
        }
        return minLength;
    }

    private static String getCommonPrefix(String[] strs) {
        int len = getMinLength(strs);
        int index = 0;

        for(int i=0;i<len;i++) {
            for(int j=1;j<strs.length;j++) {
                if(strs[0].charAt(i) != strs[j].charAt(i)) {
                    return strs[0].substring(0, index);
                }
            }
            index++;
        }

        return strs[0].substring(0, index);
    }

    public static void main(String[] args) {
        String[] strs = {"prasad", "praweq", "pravin"};
        System.out.println(getCommonPrefix(strs));
    }
}