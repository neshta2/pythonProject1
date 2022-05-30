a = ["hey", "hello", "goodbye"]
# print(a[0])
# print(a[1])
# print(a[2])
for element in a:
    print(element)

b = [20, 30, 50, 60]
for num in b:
    print(num)

total_sum = 0
for e in b:
    total_sum = total_sum + e
print(total_sum)

total_sum2 = 0
for i in range(1, 5):
    total_sum2 += i
print(total_sum2)

print(list(range(1, 100)))
total_sum3 = 0
for f in range(1, 100):
    total_sum3 += f
print(total_sum3)

total_sum4 = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total_sum4 += i
print(total_sum4)

