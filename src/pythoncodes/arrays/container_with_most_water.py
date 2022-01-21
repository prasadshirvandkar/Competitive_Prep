def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        h = min(height[left], height[right])
        max_area = max(max_area, h * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


if __name__ == '__main__':
    arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    arr1 = [1, 1, 1, 1, 1, 1, 1]
    arr2 = [4, 3, 2, 1, 4]
    arr3 = [1, 3, 2, 1, 4]
    arr4 = [0, 2]
    arr5 = [1, 2, 4, 3]
    print(maxArea(arr1))
