""" palindrome numbers """
a = 20
b = 20
ters = 0
while (True):
    sayi = a * b
    gecici = sayi
    while (sayi > 0):
        kalan = sayi % 10
        ters = ters * 10 + kalan
        sayi = sayi / 10
    if (ters == sayi):
        print(str(gecici) + " palindromdur")
        break
    else:
        if (a >= b):
            a -= 1
        else:
            b -= 1
