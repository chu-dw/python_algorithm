'''현우는 용돈을 효율적으로 활용하고 돈을 펑펑 쓰지 않기 위해서 앞으로 N일 동안 자신이 매일 사용할 금액을 계산하고,
정확히 통장에서 M번, K원 씩 출금해서 사용하기로 결정했습니다.
현재 수중에 있는 금액으로 하루를 보낼 수 있다면 그대로 소비합니다.
부족하다면, 수중에 있는 금액은 통장에 넣은 뒤 K원을 인출해서 하루를 생활합니다.
 이때, 현우가 매번 출금할 금액 K원의 최솟값을 구하는 프로그램을 작성해주세요.'''
use = []
answer = 0
N, M = map(int,input().split())

for i in range(N):
    k = int(input())
    use.append(k)

start, end = min(use), sum(use)
while start <= end:
    mid = (start+end) // 2
    charge = mid
    num = 1
    for i in range(N):
        if charge < use[i]:
            charge = mid #충전
            num+=1
        charge -= mid

    if num > M or mid < max(use):
        start = mid+1
    else:
        end = mid-1
        answer = mid

print(answer)