while 1:
    ans = 0
    city_from = []
    city_go = []
    s = int(input())

    if s != "":
        for i in range(s):
            S_a, S_b = input().split()
            city_from.append(S_a)
            city_go.append(S_b)
        temp = []
        for i in range(s):
            if len(city_from) != 0:
                temp.append(city_from[i])
                if city_go[i] in temp:
                    ans += 1
                    temp = []
        print(ans)

    else:
        break