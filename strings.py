name = 'Berfin'
surname = "Celik"
age = 26

greeting = 'My name is ' + name + ' ' + surname + ' and \nI am ' + str(age) + ' years old.' # ters slash  + n (\n) yeni satıra geçer.

print(greeting[0]) # 0. index yani 1. karakter : M harfini vericek
print(greeting[3])
print(greeting[6])

print(len(greeting)) # len : ifadenin kaç karakterli oldugunu verir.
print(greeting[len(greeting) - 1])
print(greeting[-1]) # burda da son harfi veriyor.
print(greeting[2:5]) # 2. indexten 5. i indexe kadar (  : ( na))
print(greeting[3:]) # 3 ten başladı sonuna kadar gitti , kesmedi
print(greeting[:17]) # baştan başlar 17. ifadeye akdar gider
print(greeting[2:40:2]) # 2  den 40. karaktere kadar git ancak her karakterı alma , 2 karakterde bir al.