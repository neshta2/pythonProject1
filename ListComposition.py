a = [1, 2, 3, 4, 5]

l = []
l.append(1)
l.append(2)
print(l)

b = []
for num in a:
    b.append(num * 2)

print(b)

c = [num * 2 for num in a]
print(c)

range_elements = []
for num in range(1, 6):
    range_elements.append(num * 3)
print(range_elements)

range3 = [num * 3 for num in range(1, 6)]
print(range3)

a = [1, 10, 12, 4, 3, 20, 55]

a_filtered = []
for num in a:
    if num < 10:
        a_filtered.append(num)
print(a_filtered)

a_filtered = [num for num in a if num < 10]
print(a_filtered)

a_filtered_squared = [num ** 2 for num in a if num < 10]
print(a_filtered_squared)

words = ["hello", "hey", "goodbye", "guitar", "piano"]
words_filtered = [word for word in words if len(word) < 6]
print(words_filtered)


