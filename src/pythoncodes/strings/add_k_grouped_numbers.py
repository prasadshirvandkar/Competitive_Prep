def add_k_grouped_numbers(num, k):
    if len(num) <= k:
        return num

    while len(num) > k:
        curr = 0
        curr_num = ''
        for i in range(len(num)):
            if i != 0 and i % k == 0:
                curr_num += str(curr)
                curr = 0
            curr += int(num[i])
        curr_num += str(curr)
        num = str(curr_num)

    return num


if __name__ == '__main__':
    number = "1111122222"
    group = 5
    print(add_k_grouped_numbers(number, group))
