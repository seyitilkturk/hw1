"""

Kullanıcıdan alınan 10 sayının çift ve tek sayıların sayısını
ekrana yazdıran programı yazınız.

"""
even_num = 0
odd_num = 0

for i in range(10):
    temp = input("Enter number %d: " % (i+1))
    if int(temp) % 2 == 0:
        even_num += 1
    else:
        odd_num += 1

print("The number of even numbers => %d" % even_num)
print("The number of odd numbers => %d" % odd_num)
