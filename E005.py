"""
Girilen bir metnin son 2 karakterini 4 defa çoğaltarak ekrana yazan
Python programını yazınız. * aritmetik operatöründen faydalanabilirsiniz.
"""

given_text = input("Enter a text: ")
print(4 * ("%s %s\n" %(given_text[-2], given_text[-1])))
