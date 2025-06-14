n = int(input())

v = []
d = {}

for i in range(n):
    x, y = list(map(int, input().split()))
    v.append((x, y))

for j in range(len(v)):
    w = v[j]
    l = w[1]
    if l not in d:
        d[l] = []
    d[l].append(w)

def get_x(t):
    return t[0]

for k in d.keys():
    d[k].sort(key=get_x)

lsls = list(d.keys())
lsls.sort()

for l in lsls:
    for m in d[l]:
        print(m[0], m[1])
