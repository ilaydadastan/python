sayi_toplam=0
for sayi in range(0,1000): """ In the for, the range to be processed is written. """
    if sayi%3==0 or sayi%5==0: """ Numbers divisible by both 3 and 5 can be subtracted at the same time using "or". """
        sayi_toplam=sayi_toplam+sayi    
print(sayi_toplam)
