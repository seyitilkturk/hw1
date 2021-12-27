"""
Kullanıcı tarafından girilen bir kelimenin palindrom olup olmadığını karşılaştırma
operatöründen faydalanarak print() fonksiyonu ile ekrana yazdırınız
"""

given_text = input("Enter a word to test whether it is palindrome or not: ").lower()

if given_text == given_text[::-1]:
    print("This word is palindrome.")
else:
    print("This word is not palindrome.")

