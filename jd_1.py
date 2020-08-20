while 1:
    ans = 0
    s = input()

    if s != "":
        for x in s.split():
            n = int(x)
            if n <= 0:
                print(0)
            else:
                res = 0
                for i in range(1, n + 1):
                    temp1 = 5 * (2 * n - 1)
                    temp2 = 5 * 2 * n
                    res = res + 1 / temp1 -1/temp2

                res = round(res, 4)
                print(res)
    else:
        break