T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # num : 연속으로 커지는 당근의 개수
    # max_num : 연속으로 커지는 당근의 개수의 최댓값
    num = 1
    max_num = 1

    # i + 1 번째보다 i 번째 당근의 개수가 커지면 num을 증가
    for i in range(N - 1):
        if arr[i + 1] > arr[i]:
            num += 1
        else:
            num = 1

        # num이 max_num보다 크면 max_num 값 교환
        if num > max_num:
            max_num = num

    print(f"#{tc} {max_num}")
