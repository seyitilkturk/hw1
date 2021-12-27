"""

Bir metin içerisindeki büyük ve küçük harflerin listesini yazdıran python programını yazınız.

"""

my_list = ["a", "B", "C", "d", "e", "X", "Y", "z", "f"]
lowercase_list = list()
uppercase_list = list()

for i in my_list:
    if i.islower():
        lowercase_list.append(i)
    elif i.isupper():
        uppercase_list.append(i)

print("lowercase letters => " + repr(lowercase_list))
print("uppercase letters => " + repr(uppercase_list))
