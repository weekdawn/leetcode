import sys

def getAns(K, N, n_list):
    if K == 0:
        return "parabox"
    if N == 0:
        return K, 0
    # 保存骰子和
    res = 0
    # 记录回退次数
    ntime = 0
    for i in range(N):
        res += n_list[i]
        if res == K and i < N-1:
            return "parabox"
        #每次回退更新距离和骰子和
        if res > K:
            ntime += 1
            disc = res - K
            res = K - disc
    if res < K and ntime == 0:
        disc = K -res
        return disc, 0
    if ntime != 0:
        return disc, ntime

if __name__ == "__main__":
    # 读取第一行的n
    firstline = sys.stdin.readline().strip()
    K, N = map(int, firstline.split())
    # 读取第2行
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    ans = getAns(K, N, values)
    print(ans)





