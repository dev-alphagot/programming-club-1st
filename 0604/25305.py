n, c = list(map(int, input().split()))

v = list(map(int, input().split()))
s = []

for j in range(n):
    m = max(v)
    s.append(m)
    v.remove(m)

print(s[c - 1])