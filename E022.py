"""

Girilen on sayı içerisinden en büyük üç sayıyı bulmak için bir Python fonksiyonu yazınız.

"""

def find_largest_three(my_list):
    my_list.sort()
    print(my_list[:-4:-1])


find_largest_three([10, 3, 7, 90, 4, 44, 55, 80, 3, -10])




