website = "http://www.berfincelik.com"
course = "Python Kursu : Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
a = ' Hello World '.strip()
a = ' Hello World '.lstrip() #soldan boşluk sildik
a = ' Hello World '.rstrip() #sağdan boşluk sildik

#2- 'www.berfincelik.com' içindeki berfincelik bilgisi hariç her karakteri sil.
a = 'www.berfincelik.com'
a = a.strip('w.com')

#3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
a = course.lower()

#4- 'website' içinde kaç tane 'a' karakteri vardır ? 
print(website.count('a')) #0

#5- 'website' www ile aşlayıp com ile bitiyor mu ?
isFound = website.startswith('www') #true
isFound = website.endswith('com') #true

#6- 'website' içinde '.com' ifadesi var mı ?
a = website.find('.com') #22

#7- 'course' içindeki karakterlerin hepsi alfabetik mi ? (isalpha, isdigit)
a = course.isalpha() #Alfabetik mi ? False (sayısal değer de var) 
a = 'Hello'.isalpha() #True 
a = course.isdigit() #Sayısal mı ? False (yazısal değerler var)
a = '123'.isdigit() #True

#8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna '*' ekleyiniz
a = 'Contents'.center(50,'*')
a = 'Contents'.ljust(50, '*') #soluna ekledik
a = 'Contents'.rjust(50,'*') #sağına ekledik

#9- 'course' karakter dizisindeki tüm boşluk karakterini '-' ile değiştirin
a = course.replace(' ','-')
a = course.replace(' ', '-',5) # sadece 5 karaktere uyguladı.

#10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin.
a = 'Hello World'.replace('World','There')

#11- 'course' karakter dizisinin boşluk karakterrlerinden ayırın.
a = course.split(' ')

print(a)

