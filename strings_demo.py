website = "http://www.celikberf.com"
course = "Python Kursu : Baştan Sona Python Programlama Rehberiniz (40 saat)"
name, surname, age, job = "Berfin" , "Çelik" , 26 , "mühendis"

#1- 'course' karakter dizisinde kaç karakter bulunmaktadır ? 
#2- 'website' içinden www karakterlerini alın .
#3- 'website' içinden com karakterlerini alın.
#4- 'course' içinden ilk 15 ve son 15 karakterlerini alın
#5- 'course' ifadesindeki karakterleri tersten yazdırın. 
#6- "Benim adım Berfin Çelik , Yaşım 26 ve mesleğim mühendis."
#7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
#8- 'abc' ifadesini yan yana 3 defa yazdırın.

#1 
result = len(course)
length = len(website)

#2
result = website[7:10]

#3
result = website[length-3 : length]

#4
result = course[:15]
result = course[-15:]

#5
result = course[::-1]

#6
result = "Benim adım "+ name + " " + surname , " Yaşım " + str(age) + " ve mesleğim " + job
result = "Benim adım {} {}, Yaşım {} ve mesleğim {}.".format(name,surname,age,job)
result = f"Benim adım {name} {surname} , Yaşım {age} ve mesleğim {job}."

#7
s = 'Hello world'
s = s[0:6] + 'W' + s[-4:]
s.replace('w','W') # w gördüğün yere W koy

#8
result = 'abc ' * 3

print(s)
print(result)

