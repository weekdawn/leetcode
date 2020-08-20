while 1:
    ans = 0
    s = input()
    N, X = s.split()
    grade_day = []

    if s != "":
        for _ in range(int(N)):
            grade, day = input().split()
            grade_day.append([int(day), int(grade)])
        grade_day = sorted(grade_day)
        days_count = 0
        res = 0
        for i in range(int(N)):
            days_count += grade_day[i][0]
            res += grade_day[i][1]
            if days_count <= int(X):
                if res >= ans:
                    ans = res
            else:
                temp = days_count - grade_day[i][0]
                if grade_day[i][1] > grade_day[i-1][1] and temp - grade_day[i-1][0] + grade_day[i][0] <= int(X):
                    days_count -= grade_day[i-1][0]
                    res -= grade_day[i-1][1]
                    ans = res
                else:
                    days_count -= grade_day[i][0]
                    res -= grade_day[i][1]
        print(ans)
    else:
        break