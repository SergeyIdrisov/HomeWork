shit = int(input())
r = set()
l = set()
for i in range(shit):
    a1,a2 = list(map(int, input().split()))
    r.add(a1)
    l.add(a2)
ans = 0
for i in r:
    if i not in l:
       ans +=1
print(ans)