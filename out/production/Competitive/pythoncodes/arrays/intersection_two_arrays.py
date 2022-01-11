def intersection(nums1, nums2):
    intersect = []
    n1, n2 = len(nums1), len(nums2)
    i, j = 0, 0

    while i < n1 and j < n2:
        if nums1[i] == nums2[j]:
            intersect.append(nums1[i])
            i += 1
            j += 1
        elif n1 < n2:
            j += 1
        else:
            i += 1

    return intersect


if __name__ == '__main__':
    arr1 = [4, 9, 5, 9]
    arr2 = [9, 4, 9, 8, 9]

    print(intersection(arr1, arr2))
