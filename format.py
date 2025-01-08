name = "Berfin"
surname = "Celik"
age = 25

# print('My name is {} {}'.format(name , surname)) # 2 parametre verdik . {} ' ler ile daha da kolaylaştırabiliriz.
# print('My name is {1} {0}'.format(name , surname)) # index yerlerini değiştirdik 'celik berfin' yaptı.
# print('My name is {s} {n}'.format(n = name , s = surname)) # 'celik berfin' verdi. Yerlerini değiştirdik diye.
# print('My name is {} {}and I am {} years old.'.format(name , surname , age)) # yaş bilgisini ekledik

# result = 200 / 700

# print('The result is {r:1.3} ' .format(r = result)) # 3 bilgisi virgülden sonra kaç basamagı temsil ediyor. 1 kısmı da kaç karakterlik boşluk bıraktığı.

print(f'My name is {name} {surname} and I am {age} years old.')
