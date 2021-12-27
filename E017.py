"""
Bir listeyi bir sözlükte sıralamak için bir Python programı yazın
Örnek Veri: num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

"""

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}


for i in range(len(num)):
    list(num.items())[i][1].sort()

print(num)


