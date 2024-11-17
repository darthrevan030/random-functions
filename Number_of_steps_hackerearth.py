num = int(input())
str1 = list(map(int, input().split()))
str2 = list(map(int, input().split()))

min_= min(str1)

count = 0

j = 0

while j < num:
    if str1[j] >= str2[j]:
        while str1[j] > min_:
            str1[j] -= str2[j]
            count += 1
    if str1[j] < min_:
        min_diff = str1[j]
        j = 0
    if str1[j] != min_:
        count -= 1
        break

    j += 1

print(count)