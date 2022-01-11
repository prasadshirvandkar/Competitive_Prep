package javacodes.String;

public class Palindrome {
    
    public static boolean isPalindrome(String s) {
        if(s == null) return false;
        
        if(s.length() == 1 || s.equals("") || s.equals(" ")) return true;
        
        s = s.toLowerCase();
        
        int left = 0;
        int right = s.length() - 1;

        while(left < right) {
            char c1 = s.charAt(left);
            char c2 = s.charAt(right);

            if(Character.isLetter(c1) && Character.isLetter(c2)) {
                if(c1 != c2) {
                    return false;
                }
                left++;
                right--;
            }

            if(!Character.isLetter(c1)) left++;
            if(!Character.isLetter(c2)) right--;
        }
        
        return true;
    }

    public static void main(String[] args) {
        String s = "madam";

        System.out.println(isPalindrome(s));
    }
}