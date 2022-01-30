def allocate_books(books_with_pages, s):
    left = min(books_with_pages)
    right = sum(books_with_pages)
    count = 1
    mn = right
    while left <= right:
        mid = (left + right) // 2
        sm = 0
        for b in books_with_pages:
            if sm + b >= mid:
                count += 1
                sm = 0
            sm += b

        if count >= s:
            left = mid + 1
        else:
            mn = mid
            right = mid - 1

        count = 0

    print(mn - 1)


if __name__ == "__main__":
    books_with_p = [12, 34, 67, 90]
    books_with_p1 = [10, 20, 30, 40]
    s = 2
    allocate_books(books_with_p1, s)
