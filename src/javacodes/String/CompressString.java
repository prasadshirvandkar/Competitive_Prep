package javacodes.String;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

class CompressString {
    public static String compress_string(String inp) {
        String compressed = "";
        Pattern pattern = Pattern.compile("([\\w])\\1*");
        Matcher matcher = pattern.matcher(inp);
        while(matcher.find()) {
           String group = matcher.group();
           if (group.length() > 1) compressed += group.length() + "";
           compressed += group.charAt(0);
        }
        return compressed;
    }

    public static void main(String[] args) {
        System.out.println(compress_string("AAAABBBCCCCCCCAAA"));
    }
}