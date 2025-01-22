# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi  , dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçka açtığımızı belirtir.

# "w"  : (write) yazma modu. Dosya konumda oluşturur.
#       ** Dosya içeriğini siler ve yeniden ekleme yapar.
"""

file  = open("newfile.txt", "w")  # sol dosyalara newfile text ekledik
file = open("/Users/berfin/Desktop/newfile.txt","w") # masaüstüne newfile text diye dosya açtık
file.close() #  dosya arka planda çalışmaya devam etmesin diye dosyayı kapattık

file = open("newfile.txt","w")
file.close()

file.write("Berfin Celik")
file.close

"""

# "a"  : (append) ekleme. Dosya konumda yoksa oluşturur.
"""
file = open("newfile.txt","a")
file.write(" Berfin Celik\n")
file.close()

"""
# "x"  : (create) oluşturma. Dosya zaten varsa hata verir.

"""
file = open("newfile2.txt","x")
"""
# "r"  : (read) okuma. Varsayılan dosya konumda yoksa hata verir.

"""
try:
    file = open("newfile.txt","r")
    print(file)
except FileNotFoundError:
    print("dosya okuma hatası")
finally:
    print("dosya kapandı.")
    file.close()
"""
"""
file = open("newfile.txt","r")

#for döngüsü

for i in file:
    print(i, end="")
file.close()

"""
"""
file = open("newfile.txt","r")
content = file.read()

print("içerik 1")
print(content)

print("içerik 2")
content2 = file.read()
print(content2)

file.close()

"""
"""
file = open("newfile.txt","r")
content = file.read(5)
print(content)

file.close
"""
"""

file = open("newfile.txt","r")
print(file.readline(),end = "")
print(file.readline(),end = "")
print(file.readline(),end = "")
print(file.readline(),end = "")

file.close()
"""

"""
file = open("newfile.txt","r")
liste = file.readlines() # diziye çevirdi
print(liste)

file.close()

"""