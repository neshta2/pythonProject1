total = 0
for i in range(1, 5):
    total += i
print(total)

total2 = 0
i1 = 0
while i1 < 5:
    total2 += i1
    i1 += 1
print(total2)

my_list = [7, 5, 4, 4, 3, 2, 1]

# while
total3 = 0
i2 = 0
while i2 < len(my_list) and my_list[i2] > 0:
    total3 += my_list[i2]
    i2 += 1
print(total3)

# for
# total4 = 0
# for element in my_list:
#    if element <= 0:
#        break
#    total4 += element
# print(total4)

########################
total5 = 0
i5 = 0
while total5 < 10 and my_list[i5] > 0:
    total5 += my_list[i5]
    i5 += 1
print(total5)

i6 = 0
while True:
    if i6 == 100:
        break
    print(i6)
    i6 += 1

names = ["Mike", "Tom", "Katy", "Alex"]
for elements in names:
    print(elements)
for i in range(0, 3):
    print(names[i])
