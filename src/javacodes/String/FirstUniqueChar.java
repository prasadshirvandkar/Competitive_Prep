package javacodes.String;

public class FirstUniqueChar {
    public static void main(String[] args) {
        String s = "loveleetcode";
        int[] freq = new int[26];
        
        for(char c: s.toCharArray()) {
            freq[c - 'a']++; 
        }

        int index = -1;
        for(int i=0;i<s.length();i++) {
            if(freq[s.charAt(i) - 'a'] == 1) {
                index = i;
                break;
            }
        }
        
        System.out.println(index);
    }
}