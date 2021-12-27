"""
Kullanıcıdan değişecek metin ve eski harf ve yeni harf bilgisini alarak girilen metin üzerinden
değişikliği yapıp sonucu ekrana yazdıran Python programını yazınız.
"""

given_text = input("Enter a text: ")
old_char = input("Enter old char: ")
new_char = input("Enter new char: ")
final_text = given_text.replace(old_char, new_char)
print(final_text)

