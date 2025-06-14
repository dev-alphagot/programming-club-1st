n = int(input())

v = []
d = {}

for i in range(n):
    r = input()
    if r not in v:
        v.append(r)


for j in range(len(v)):
    w = v[j]
    l = len(w)
    if l not in d:
        d[l] = []
    d[l].append(w)

for k in d.keys():
    d[k].sort()

lsls = list(d.keys())
lsls.sort()

for l in lsls:
    for m in d[l]:
        print(m)
