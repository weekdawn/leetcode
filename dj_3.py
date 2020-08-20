while 1:
    ans = 0
    s = input()
    k = int(input())

    if s != "":
        if not s or k <= 0:
            print(s)
        if len(s) == k:
            print(0)
        num_stack = []
        for value in s:
            while k and num_stack and value < num_stack[-1]:
                num_stack.pop()
                k -= 1
            num_stack.append(value)
        while k:
            num_stack.pop()
            k -= 1
        print(str(int("".join(num_stack))))

    else:
        break