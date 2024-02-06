def quick_merge(list1, list2):
    result = []
    p1 = 0
    p2 = 0
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):
        result += list1[p1:]
    else:
        result += list2[p2:]
    return result

n = int(input())
merged_list = []
lists = []
for _ in range(n):
    nums = input().split()
    nums = [int(num) for num in nums]
    lists.append(nums)

if n > 0:
    merged_list = lists[0]
    for i in range(1, n):
        merged_list = quick_merge(merged_list, lists[i])

output = ' '.join(map(str, merged_list))
print(output)

# вводим числ - кол-во  и вводим числа через пробел , в итоге сортированный список
