T = int(input())

grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    # 모든 학생의 총점을 저장할 리스트
   scores = []


    for i in range(N):
        mid, final, homework = map(int, input().split())

        # 중간 35%, 기말 45%, 과제 20%
        total = mid * 0.35 + final * 0.45 + homework * 0.2

        # (총점, 학생 번호)를 함께 저장
        scores.append(total)

    # k번째 학생의 점수 저장
    target = scores[K - 1]

    # 총점이 높은 학생부터 정렬
    scores.sort(reverse=True)

    rank = scores.index(target)

    # k번째 학생의 등수
    rank = 0

    # 한 평점에 몇명인지 계산
    grade_cnt = N // 10

    index = rank // grade_cnt

    answer = grades[index]

    print(f"#{tc} {answer}")
