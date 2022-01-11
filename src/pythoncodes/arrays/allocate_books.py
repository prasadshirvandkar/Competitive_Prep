def allocate_books():
    books_with_pages = [12, 34, 67, 90]
    s = 2

    left = min(books_with_pages)
    right = sum(books_with_pages)
    count = 1
    mn = right
    while left <= right:
        mid = (left + right) // 2
        print(mid)
        sm = 0
        for b in books_with_pages:
            if sm + b > mid:
                count += 1
            sm += b

        if count > s:
            left = mid + 1
        else:
            mn = mid
            right = mid - 1

        count = 0

    print(mn)


if __name__ == "__main__":
    allocate_books()
