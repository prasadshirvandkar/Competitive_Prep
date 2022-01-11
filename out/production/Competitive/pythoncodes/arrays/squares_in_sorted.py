def squares_in_sorted(nums):
    squares = []
    i, j = 0, len(nums) - 1

    while i <= j:
        if abs(nums[i]) > abs(nums[j]):
            squares.append(pow(nums[i], 2))
            i += 1
        else:
            squares.append(pow(nums[j], 2))
            j -= 1

    squares.reverse()
    return squares


if __name__ == '__main__':
    arr = [-7, -3, 2, 3, 11]
    arr1 = [-4, -1, 0, 3, 10]
    print(squares_in_sorted(arr))
