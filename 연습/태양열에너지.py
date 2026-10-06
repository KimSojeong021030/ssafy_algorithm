T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    panel = [list(map(int, input().split())) for _ in range(N)]
    lens = [list(map(int, input().split())) for _ in range(M)]

    answer = []

    for i in range(N - M + 1):
        row = []
        for j in range(N - M + 1):

            sum_v = 0

            for r in range(M):
                for c in range(M):
                    sum_v += panel[i + r][j + c] + lens[r][c]

            row.append(sum_v)

        answer.append(row)

    print(f"#{tc}")

    for row in answer:
        print(*row)