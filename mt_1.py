while 1:
    ans = 0
    pre = []
    beh = []
    s = int(input())

    if s != "":
        # print("2345" == "2345")
        s //= 4
        for i in range(1, s):
            if len(str(i)) == len(str(i * 4)):
                if str(i) == str(i * 4)[::-1]:
                    ans += 1
                    pre.append(i)
                    beh.append(int(str(i * 4)[::-1]))
        print(ans)
        for i in range(ans):
            print("%d %d" % (pre[i],  beh[i]))
    else:
        break