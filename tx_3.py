if __name__ == "__main__":
    ans = 0
    T = int(input())

    for i in range(T):
        n = int(input())
        max_x = 0
        half = int(n/2)
        for a in range(half+1):
            b = n - a
            al = [int(x) for x in str(a)]
            bl = [int(x) for x in str(b)]
            total = al + bl
            sum_x = 0
            for i in total:
                sum_x += i
            if sum_x >= max_x:
                max_x = sum_x
        print(max_x)
