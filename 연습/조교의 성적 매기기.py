T = int(input())

grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    scores = []

    for i in range(N):
        mid, fin, hom = map(int, input().split())

        total = mid * 0.35 + fin * 0.45 + hom * 0.2

        scores.append(total)

    target = scores[K - 1]

    scores.sort(reverse=True)

    rank = scores.index(target)

    grades_cnt = N // 10

    index = rank // grades_cnt

    answer = grades[index]

    print(f"#{tc} {answer}")