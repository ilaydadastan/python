sonuc = 0
toplam1 = 0
toplam2 = 0
kuvvet = 0
sayi = 0
for a in range(1, 101):
    sayi = a * a
    toplam1 = toplam1 + sayi

for b in range(1, 101):
    toplam2 = toplam2 + b
kuvvet = toplam2 * toplam2

if kuvvet > toplam1:
    sonuc = kuvvet - toplam1
else:
    sonuc = toplam1 - kuvvet

print(sonuc)
