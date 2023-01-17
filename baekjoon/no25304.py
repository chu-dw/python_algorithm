total = input()
num = input()
total_check = 0
for i in range(int(num)):
    check_p, check_n = input().split()
    total_check = total_check + (int(check_p) * int(check_n))


if total_check == int(total):
    print('Yes')
else:
    print('No')

#input 받을 때 int변환이 편할 듯