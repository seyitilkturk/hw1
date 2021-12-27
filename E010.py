""" liste1 = ["1",1,2,"3"] Yukarıdaki listenin bir kopyasını alarak 250 sayısını listenin
sonuna ekleyiniz,her iki listeyi ekrana yazdırınız.
Beklenen Çıktı: ["1",1,2,"3"] => Liste1 Çıktısı ["1",1,2,"3",250] => Liste2 Çıktısı

"""

list1 = ["1", 1, 2, "3"]
list2 = list1.copy()
list2.append(250)

print(repr(list1) + " => List1")
print(repr(list2) + " => List2")
