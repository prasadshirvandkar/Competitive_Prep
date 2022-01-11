package javacodes.String;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class PermuteString {
    static Set<String> stringSet = new HashSet<>();
    static StringBuilder sBuilder = new StringBuilder();

    static void permuteString(String s) {
        int[] count = new int[26];
        for(char c: s.toCharArray()) { count[c - 'a']++; }
        char[] result = new char[s.length()];
        permute(s, count, result, 0);
        printHashSet();
    }

    private static void permute(String s, int[] count, char[] result, int level) {
        if(level == result.length) {
            printArray(result);
            return;
        }

        for(char c: s.toCharArray()) {
            if(count[c - 'a'] == 0) {
                continue;
            }
            result[level] = c;
            count[c - 'a']--;
            permute(s, count, result, level + 1);
            count[c - 'a']++;
        }
    }

    private static void printArray(char[] result) {
        for(char c: result) {
            sBuilder.append(c);
        }
        stringSet.add(sBuilder.toString());
        sBuilder.delete(0, result.length);
    }

    private static void printHashSet() {
        Iterator<String> itr = stringSet.iterator();
        while(itr.hasNext()) {
            System.out.println(itr.next());
        }
    }

    public static void main(String[] args) {
        permuteString("aabc");
    }
}