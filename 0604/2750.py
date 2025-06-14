n = int(input())

v = []
s = []

for i in range(n):
    v.append(int(input()))

for j in range(n):
    m = min(v)
    s.append(m)
    v.remove(m)

for k in s:
    print(k)