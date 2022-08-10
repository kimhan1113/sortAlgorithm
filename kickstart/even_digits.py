import sys
T = int(sys.stdin.readline())

for test_case in range(1,T+1):
    N = sys.stdin.readline().rstrip()
    start = len(N)
    for i, ch in enumerate(N):
        if int(ch) % 2 == 1:

            start = i
            break

    N = N[start:]        
    # print(f"N: {N}")

    if not N:
        print(f"Case #{test_case}: 0")
        continue

    n = len(N)
    init = N[0]
    candidates = ["0", "2", "4", "6", "8", "8" * n, "8" * (n-1), "2" + "0" * n, "2" + "0" * (n-1)]

    if init != "1":
        candidates.append(str(int(init)-1) + "8" * (n-1))

    if init != "9":
        candidates.append(str(int(init)-1) + "0" * (n-1))

    answer = min([abs(int(N) - int(candidate)) for candidate in candidates if candidate])
    print(f"Case #{test_case}: {answer}")