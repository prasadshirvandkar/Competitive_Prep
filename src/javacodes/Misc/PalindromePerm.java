package javacodes.Misc;

import java.util.HashMap;
import java.util.Map;

public class PalindromePerm {
    public static void main(String[] args) {
        String s = "Tact Coa";
        s = s.toLowerCase();

        Map<Character, Integer> map = new HashMap<>();

        for(char c: s.toCharArray()) {
            if ('a' <= c && c <= 'z') {
                map.put(c, (map.containsKey(c)) ? map.get(c) + 1 : 1);
            }
        }

        boolean foundOdd = false;
        for(Map.Entry<Character, Integer> charsMap: map.entrySet()) {
            if (charsMap.getValue() % 2 == 1) {
                if(foundOdd) {
                    foundOdd = false;
                    break;
                }
                foundOdd = true;
            }
        }

        System.out.println(foundOdd);
    }
}