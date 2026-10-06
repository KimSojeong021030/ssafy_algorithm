T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    AN = list(map(int, input().split()))

    satisified = True

    for i in range(N-1):
        if AN[i] > AN[i+1]:
            satisified = True
        else:
            satisified = False
            break

    if satisified == True:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")