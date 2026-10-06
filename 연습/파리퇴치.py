T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):

            kill = 0

            for r in range(M):
                for c in range(M):
                    kill += arr[i + r][j + c]

            if kill > max_kill:
                max_kill = kill

    print(f"#{tc} {max_kill}")