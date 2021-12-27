"""
İki farklı listede tutulan verileri tek bir listede sırasıyla append,extend metodlarıyla ve "+"
operatörü ile birleştiren python kodunu yazınız liste1 = [1,2,3] liste2 = [4,5,6] liste3 = ?????

"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list()

print("Ways to Concatenate Two Lists")


# with + operator
print("Method 1: With + operator: ")
list3 = list1 + list2
print(list3)

# with append
print("Method 2: With append method: ")
list3.clear()
[list3.append(num) for num in list1]
[list3.append(num) for num in list2]
print(list3)

# with extend
print("Method 3: With extend method: ")
list3.clear()
list1.extend(list2)
list3 = list1

print(list3)





