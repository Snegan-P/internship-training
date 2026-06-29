
s1 = list("kavitha")
s2 = list("arun")

i = 0
while i < len(s1):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            s1.pop(i)
            s2.pop(j)
            i -= 1
            break
    i += 1

finals = len(s1) + len(s2)

f = list("flames")
index = 0

while len(f) != 1:
    index = (index + finals - 1) % len(f)
    f.pop(index)

print(f[0])