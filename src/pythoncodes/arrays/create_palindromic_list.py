def create_palindromic_list(sales_data):
    if len(sales_data) == 1:
        print(sales_data)

    if len(sales_data) == 2:
        first, second = sales_data[0], sales_data[1]
        print(sales_data if first == second else [first, second])

    i, j = 0, len(sales_data) - 1
    curr = 0
    new_arr = []
    while i < j:
        if sales_data[i] == sales_data[j]:
            new_arr.append(sales_data[i])
            i += 1
            j -= 1
            curr = 0
        elif sales_data[i] < sales_data[j]:
            curr += sales_data[i]
            if curr == sales_data[j]:
                new_arr.append(curr)
                j -= 1
                curr = 0
            i += 1
        else:
            curr += sales_data[j]
            if curr == sales_data[i]:
                new_arr.append(curr)
                i += 1
                curr = 0
            j -= 1

    for i in range(len(new_arr) - 2, -1, -1):
        new_arr.append(new_arr[i])

    return new_arr


if __name__ == '__main__':
    salesData = [15, 15]
    print(create_palindromic_list(salesData))
