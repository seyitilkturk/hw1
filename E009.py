"""
liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23] yukarıdaki listeden ilk 3 sayısını silip ekrana yazdırınız.

"""

list1 = [1, 2, 3, 4, 5, 6, 7, 1, 3, 3, 3, 2, 2, 1, 23]
removed_items = list1[:3]
del list1[:3]
print(list1)
print(removed_items)



