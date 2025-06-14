v = list(map(ord, list(input())))
s = []

for j in range(len(v)):
    m = max(v)
    s.append(m)
    v.remove(m)

print("".join(list(map(chr, s))))