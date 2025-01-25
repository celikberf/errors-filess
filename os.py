import os
import datetime

result = dir(os) # işletim sistemiyle alaakalı bilgi sunar. dosyalarla ilgili işlemler yapabiliriz.
result = os.name #işletim sistetmini söyler (posix)
result = os.getcwd() # bulunduğumuz dosya hakkında bilgi (Users/berfin/Desktop/04.12.24 Python/Python_Temellerri)
# os.mkdir('newdirecory') # newdirectory diye klasör oluşurur 
# os.chdir('..') # bi önceki klasöre geçer
# os.makedirs('newdirector/yyeeniklasor') # iç içe klasör olusturur
# os.rename('newdirectory/yeniklasör') # klasötün  ismini değiştirebiliriz.
# os.rmdir('newdirectory') # ilgili klasörü sileriz . remove

# result = os.listdir() # klasör veya dosyaların hepsini listeler.
# for dosya in os.listdir():
#     if dosya.endswith('.py'): # sadeece .py uzantılı dosyaları listtelemiş olduk
#         print(dosya)
# result = os.stat('datetime.py') # oluşturulma değiştirilme tarihi vb.
# result = result.st_size/1024 # byt ı
# result = datetime.datetime.fromtimestamp(result.st_ctime)  # dosyanın oluşturulma zamanı
# result = datetime.datetime.fromtimestamp(result.st_atime)  # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)  # değiştirilme tarihi
# os.system(notepad.exe) #not deftteri dosyası açılır

#path: (bir dosyanın uzantısıını ismini nasıl değiştiririz vb.)
# result = os.path.abspath('os.py') #dosyanın tam konumu
# result = os.path.dirname('dosya tam konumu vee yolu')
# result = os.path.dirname(os.path.abspath('os.py')) #dosytanın tam yolu içrisinn dizin ismi alıyor
# result = os.path.exists('ps.py')  # ilgili  konumda doya var mı yok mu
# result = os.path.isdir('dosya tam konumu vee yolu') # klasör müdür
# result = os.path.isfile('dosya tam konumu vee yolu') # dosya mıdır
# result = os.path.join('C:\\','deneme') # c diiziniyle denemeyi değiştir ve  söyle
# result = os.path.split('C:\\deneme') # liste seklini verir
# result = os.path.splitext('os.py') # uzantııyla resmi dğiştirdik



print(result)