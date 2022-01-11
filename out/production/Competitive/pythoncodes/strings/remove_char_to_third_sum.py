def check_num(first, second, res):
    for i in range(len(first)):
        s = first[:i] + first[(i + 1):]
        if int(s) + int(second) == int(res):
            return 'True'

    return 'False'


if __name__ == "__main__":
    f_num, s_num = '10534', '67'
    t_num = '1120'
    print(check_num(f_num, s_num, t_num))
