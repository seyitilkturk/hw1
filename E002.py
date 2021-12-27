"""
Kullanıcı tarafından girilen bir metnin ilk iki ve son iki karakterini ekrana yazdıran Python programını yazınız.
"""


given_text = input("Enter a text: ")
print("The first two letters of the given text: %s and %s" %(given_text[0], given_text[1]))
print("The last two letters of the given text: %s and %s" %(given_text[-2], given_text[-1]))