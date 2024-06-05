n = int(input())
input_list = []

for i in range(n):
    input_list.append(list(map(int, input().split())))


# print(input_list)

servers = [element for n in input_list for element in n]
# print(servers)
maxNum = max(servers)
totalCount = sum(servers)

if totalCount == 0:
    print(0)
    exit()


def checkRun(minuate, servers):
    countRun = 0
    # print('minuate', minuate)
    for i in servers:
        # print('i',i)
        if i > minuate:
            countRun += minuate
            # print('plus1',minuate)
        else:
            countRun += i
            # print('plus2', i)
    # print('----------------')
    return countRun

# print(servers, maxNum, totalCount)

start, end = 0, maxNum
result = -1

while start <= end:
    mid = (start + end) // 2

    countRun = checkRun(mid,servers)
    # print('countRun',countRun)
    percent = (countRun / totalCount) * 100
    # print('percent', percent)

    if percent >= 50:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

    # print('mid',mid)


print(result)