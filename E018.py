"""

sozluk = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']} ilgili sözlükten anahtar kısımlarında
bulunan boşlukları temizleyen python kodu yazınız.

"""

sozluk = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}

dict_len = len(sozluk)

for i in range(dict_len):
    new_key = list(sozluk.items())[0][0].replace(" ", "")
    val = list(sozluk.items())[0][1]
    del sozluk[list(sozluk.items())[0][0]]
    sozluk[new_key] = val

print(sozluk)

