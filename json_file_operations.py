import json

with open('/Users/ilaydadastan/Downloads/person.json') as f:
  data = json.load(f)

ogrenci_sayisi = 0
developer = 0
product_manager = 0
yas_toplam=0
yas_ort=0
toplam=0
for person in data:
     response= person['job']
     yas_toplam = yas_toplam + person['yas']
     if response == 'öğrenci':
         ogrenci_sayisi = ogrenci_sayisi + 1
     if response == 'developer':
         developer = developer + 1
     if response == 'product manager':
         product_manager = product_manager + 1
       
toplam= ogrenci_sayisi+developer+product_manager        
print('yaslarin toplami: '+ str(yas_toplam))
yas_ort=yas_toplam/toplam
print('yaslarin ortalamasi '+ str(yas_ort))
print('toplam kişi sayisi: ' + str(toplam))
print('toplam ögrenci sayisi: '+ str(ogrenci_sayisi))
print('toplam developer sayisi: '+ str (developer))
print('toplam product manager sayisi: ' + str(product_manager))


""" Objects in the json file are called by determining their location. 
And with the values on these invoked objects, necessary operations are performed and printed. """
