def guessNumber(n)
    l, r = 1, n
    while True:
        mid = (l + r) // 2
        res = guess(mid)

        if res > 0:
            l = mid + 1
        elif res < 0:
            r = mid - 1
        else:
            return mid
    