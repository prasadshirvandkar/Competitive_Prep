def decode_strings(s):
    st_stack = []

    i = 0
    final_string, cont = '', ''
    first = 0
    while i < len(s):
        if s[i].isdigit() or s[i] == '[':
            if i != 0 and s[i] != '[':
                st_stack.append(cont)
                cont = ''
            st_stack.append(s[i])
            if s[i] == '[':
                first += 1
        elif s[i] == ']':
            stp = cont if st_stack[-1] == '[' else st_stack.pop()
            st_stack.pop()
            num = st_stack.pop()
            first -= 1

            temp = ''
            for p in range(int(num)):
                temp += stp + final_string if first == 0 else final_string + stp
            final_string = temp
            cont = ''
        else:
            cont += s[i]
        i += 1

    return final_string + cont


if __name__ == '__main__':
    st = '3[a]2[bc]'
    st1 = 'lk3[a2[c2[d]]]er' #acddcddacddcddacddcdd
    st2 = '3[apq2[cf2[d]]]'

    pa = 'apqcfddcfddapqcfddcfddapqcfddcfdd'
    pb = 'apqcfddcfddapqcfddcfddapqcfddcfdd'

    print(decode_strings(st1))
