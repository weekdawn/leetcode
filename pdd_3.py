import sys

def getAns(nlist, mlist, T):
    if T == 0:
        return 0
    #热量和美味的字典
    kj_deli = {}
    all_deli = 0
    min_kj = nlist[0][0]
    #只吃午饭
    for n_meat in sorted(nlist):
        all_deli += n_meat[1]
        if all_deli >= T:
            return n_meat[0]
    #只吃晚饭
    for m_meat in sorted(mlist):
        all_deli += m_meat[1]
        if all_deli >= T:
            return m_meat[0]
    #两顿都吃
    for n_meat in sorted(nlist):
        for m_meat in sorted(mlist):
            all_deli += n_meat[1] + m_meat[1]
            if all_deli >= T:
                now_kj = n_meat[0] + m_meat[0]
                if now_kj < min_kj:
                    min_kj = now_kj
                return min_kj

    if all_deli < T:
        return -1


if __name__ == "__main__":
    # 读取第一行的n
    firstline = sys.stdin.readline().strip()
    N, M, T = map(int, firstline.split())
    nlist = []
    mlist = []
    for i in range(N):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        nlist.append(values)
    for _ in range(M):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        mlist.append(values)

    ans = getAns(nlist, mlist, T)
    print(nlist+ mlist)