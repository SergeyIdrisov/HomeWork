"""request = int(input())
while request!=0:
    shit = int(input())
    amount = {}
    b = list(map(int, input().split()))
    for i in range(shit):
        amount[i+1] = b[i]
    amount=amount.items()
    a= 0
    c = []
    for u,v in amount:
        for i, j in amount:
            if u<i and v<j:
                a+=v
    request-=1
    print(a)"""
'''request = int(input())
while request!=0:
    shit = int(input())
    b = list(map(int, input().split()))
    a = 1
    ans = 0
    for i in range(shit-1):
        for v in range(i+1):
            if b[i+1] > b[v]:
                ans += b[v]
    print(ans)
    request-=1'''
class Fenwick_Tree():
    def __init__ (self, data: list):
        self.data = data
        self.prefix_sum = [0]*(len(data)+1)
        i = 0
        self.prefix_sum[0] = self.data[0]
        while i < len(self.data):

            for v in range(i+1):
                if self.data[i]>self.data[v]:
                    self.prefix_sum[i] += self.data[v]
            i+=1
    def sum(self,l:int, r:int):
        return self.prefix_sum[r]-self.prefix_sum[l-1]

request = int(input())
while request!=0:
    shit = int(input())
    b = list(map(int, input().split()))
    tree = Fenwick_Tree(b)
    ans = Fenwick_Tree.sum(tree, 0, len(b)-1)
    print(ans)
    request-=1
