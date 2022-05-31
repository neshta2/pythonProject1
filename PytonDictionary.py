# d = {"Alex": 25, "Petr": 37}
# d["Kate"] = 18
# for k, v in d.items():
#    print(k)
#    print(v)
# for key, value in d.items():
#    print("Key: " + str(key) + ",value: " + str(value))
# homework1
a = ["first", 1, 2, 3, "second", 10, 20, "third", 15, 56, 70, "fourth", -50]
my_dict = {}
current_str = None
for e in a:
    if (type(e) == str):
        my_dict[e] = []
        current_str = e
    else:
        my_dict[current_str].append(e)
print(my_dict)

# homework2
my_text = "Привет как дела круг Привет супер здравствуй стол стул ложка круг"
my_dict2 = {}
for word in my_text.split():
    if word in my_dict2:
        my_dict2[word] = my_dict2[word] + 1
    else:
        my_dict2[word] = 1

print(my_dict2)

my_dict3 = {}
for word in my_text.split():
    my_dict3[word] = my_dict3.get(word, 0) + 1
print(my_dict3)
