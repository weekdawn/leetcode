if __name__ == "__main__":
    ans = 0
    n = int(input())

    an = input().split()
    an = list(map(int, an))

    def find_min(arr):
        if arr:
            res = min(arr)
            for i in range(len(arr)):
                arr[i] = arr[i] - res
            new_arr = [x for x in arr if x != 0]
            flag = True
            pos = 0
            for i in range(len(arr)):
                if flag:
                    if arr[i] == 0:
                        pos = i
                    else:
                        flag = False
            for i in range(pos):
                arr.pop(i)
            flag = True
            pos = len(arr)-1
            for i in range(len(arr), -1):
                if flag:
                    if arr[i] == 0:
                        pos = i
                    else:
                        flag = False
            for i in range(pos, len(arr)):
                arr.pop(i)
            if arr:
                zero_arr = [x for x in arr if x == 0]
                bias = len(zero_arr) + 1
                return res + bias + find_min(new_arr)
        else:
            return 0
    ans = find_min(an)
    print(ans)

