package javacodes.String;

public class ImplementStrStr {
    public static void main(String[] args) {
        String haystack = "aaaaa", needle = "bba";
        int index = 0;
        int start = 0;
        int firstIndex = -1;
        int hLength = haystack.length();
        int nLength = needle.length();
        while(start < hLength) {
            if(haystack.charAt(start) == needle.charAt(index)) {
                if(index == 0) firstIndex = start;
                index++;
                
                if(index == nLength) break;
            } else {
                if(index != nLength) {
                    index = 0;
                    firstIndex = -1;
                }
            }
            start++;
        }

        System.out.println(firstIndex);
    }
}