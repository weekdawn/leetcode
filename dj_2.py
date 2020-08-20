while 1:
    ans = 0
    s = input()
    N, X = s.split()
    grades = []
    days = []

    if s != "":
        for _ in range(int(N)):
            grade, day = input().split()
            grades.append(int(grade))
            days.append(int(day))
        days_count = 0
        res = 0
        for i in range(int(N)):
            days_count += days[i]
            res += grades[i]
            if days_count <= int(X):
                if res >= ans:
                    ans = res
            else:
                days_count -= days[i]
                res -= grades[i]
        print(ans)
    else:
        break