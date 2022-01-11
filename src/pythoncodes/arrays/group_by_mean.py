if __name__ == "__main__":
    arr = [[3, 3, 4, 2], [4, 4], [4, 0, 3, 3], [2, 3], [3, 3, 3]]
    a_dict = {}

    for i in range(len(arr)):
        mean = sum(arr[i]) / len(arr[i])
        if mean in a_dict:
            a_dict[mean].append(i)
        else:
            a_dict[mean] = [i]

    print(a_dict.values())
