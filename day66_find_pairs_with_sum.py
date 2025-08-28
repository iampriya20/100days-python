nums = list(map(int, input().split()))
target = int(input())
pairs = set()
seen = set()
for x in nums:
    y = target - x
    if y in seen:
        pairs.add(tuple(sorted((x, y))))
    seen.add(x)
print(sorted(pairs))
