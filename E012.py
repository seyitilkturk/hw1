"""
sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} Sözlükteki en son elemanı silerek ekrana
işlem sonucunu yazdırınız Beklenen Çıktı :(6,60)

"""
sozluk = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
removed_item = list(sozluk.items())[-1]
sozluk.pop(removed_item[0])
print(removed_item)
print(sozluk)



