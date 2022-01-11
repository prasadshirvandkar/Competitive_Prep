def smallest_letter_greater_than_target(letters, target):
    targetValue = ord(target)

    left = 0
    right = len(letters) - 1

    while left < right:
        mid = (left + right) // 2
        if ord(letters[mid]) < targetValue:
            left = mid + 1
        else:
            right = mid

    print(letters[(left + 1) % len(letters)])


if __name__ == '__main__':
    ltrs = ["c", "f", "j"]
    t = "k"
    smallest_letter_greater_than_target(ltrs, t)