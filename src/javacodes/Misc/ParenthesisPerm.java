package javacodes.Misc;

import java.util.HashSet;
import java.util.Set;

public class ParenthesisPerm {

    static void generatePerms(Set<String> perms, int leftCount, int rightCount, char[] str, int i) {
        if (leftCount < 0 || rightCount < leftCount) return;

        if(leftCount == 0 && rightCount == 0) {
            perms.add(String.copyValueOf(str));
        } else {
            str[i] = '(';
            generatePerms(perms, leftCount - 1, rightCount, str, i + 1);

            str[i] = ')';
            generatePerms(perms, leftCount, rightCount - 1, str, i + 1);
        }
    }

    public static void main(String[] args) {
        int brackets = 3;
        char[] str = new char[brackets * 2];
        Set<String> perms = new HashSet<>();
        generatePerms(perms, brackets, brackets, str, 0);

        for(String perm: perms) {
            System.out.println(perm);
        }
    }
}
