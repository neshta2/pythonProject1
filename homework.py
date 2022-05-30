def convert_miles_to_km(x):
    return x * 1.609344


a = convert_miles_to_km(10)
print(a)


def area(x, y):
    return x * y


b = area(2, 3)
print(b)


def numbers(x):
    y = x % 2

    if y < 1:
        return str(x) + " Число четное"
    else:
        return str(x) + " Число нечетное"


y = numbers(11)
print(y)


def function1(n, k):
    if n > 20:
        print("Больше 20")
        return (0)
    else:
        sum = 0
        for i in range(1, n + 1):
            if i % 2 == 0:
                sum += i ** k
        return (sum)


d = function1(4, 2)
print(d)

my_list = [7, 5, 4, 4, 3, 2, 1, -10, -13, -15, -18]

i1 = -1
total1 = 0
while my_list[i1] < 0:
    total1 += my_list[i1]
    i1 -= 1
print(total1)

my_list3 = [7, 5, 4, 4, 3, 2, 1, -5, -10, -13, -15, -18]

total6 = 0

for i6 in reversed(my_list3):
    if i6 >= 0:
        break
    else:
        total6 += i6

print(total6)



word_list = ["apple", "banana", "grape", "some other word", "stop", "hello", "goodbye"]

for e in word_list:
    if e == "stop":
        break
    print(e)
