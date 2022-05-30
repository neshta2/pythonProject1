a = [3, 5, 20]
print(a)
a.append("Hi!")
a.pop()
print(a[-1])
a[0] = 100
print(a)
print(a[1])
a.pop(2)
print(a)

b = ["hello", "good bye", "hey"]
temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)

b[0], b[1] = b[1], b[0]  # меняет выше
print(b)

a, b,c,d = 1, 2,3,4
print(a)
print(b)
print(c)
print(d)