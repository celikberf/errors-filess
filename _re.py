import re  # arama, 

result = dir(re) 

# re module 

str = 'Python Kursu: Python Programlama Rehberiniz | 40 saat'

# re.findall()
"""
result = re.findall('Python',str) # ['Python', 'Python']
result = len(result) # 2 ... 2 tane python ifadesi bulmuş
"""

# re.split()
"""
result = re.split(' ',str) # str içinde boşluk karakteri arıyoruz. (bosluktan ayırdı )
result = re.split('R',str) # R den ayırdı
"""

# re.sub()
"""
result = re.sub(' ','-',str) #tüm boşluk karakterlerini '-' ile değiştirir
result = re.sub('\s','-',str) #tüm boşluk karakterlerini '-' ile değiştirir
"""

# re.search()
"""
result = re.search('Python',str) # 0 dan 6 ya kadar olan index aralıgında
result = result.span() #kaçıncın index
result = result.start() # hangi karaktereden başlıyor
result = result.end() # hangi karakterde bittiyor.
result = result.group() #buldugu  ifadeyi bize gönderir
result = result.string # nerde arıyor ? 
"""

#regular expression

"""
    [] - Köşeli parantezler arasına yazılan bütün karakterler aranır.
        
        [abc] => a      : 1 match
                 ac     : 2 match
                 Python : No matches

        [a-e]  => [abcde]
        [1-5]  => [12345]
        [0-39] => [1239] 0 ile 3 arasını alır 9 sabit  kalır

        [^abc] => abc dışındaki karaktreler
        [^0-9] => rakam olmayan karkterler

"""

result = re.findall('[abc]', str) # ['a', 'a', 'a', 'b', 'a', 'a']
result = re.findall('[a-e]',str) # ['a', 'a', 'a', 'e', 'b', 'e', 'a', 'a']
result = re.findall('[0-5]',str) # ['4', '0']
result = re.findall('[^abc]', str) #  abc dısınndaki tüm karakterlre ekrana yazdırılır
result = re.findall('[^0-9]', str) # rakam harici hepsini ekrana yazdırır

"""
    . - Herhangi bir teke karakteri belirtir.

        .. => a     : No match 
              ab    : 1 match
              abc   : 1 match
              abcd  : 2 matches

"""

result = re.findall('...',str)  # 3lü gruplara ayırdık. #['Pyt', 'hon', ' Ku',...
result = re.findall('Python',str) #['Python', 'Python']

"""
    ^ - Belirtilen karakterle başlıyor mu ?

    ^a => a     : 1 match
          abc   : 1 match
          bac   : No match

"""


result = re.findall('^a',str) # []
result = re.findall('^P',str) # ['P']

"""
    $ - Belirtilen karakterle bitiyor mu ?

        a$ => a      : 1 match
              lamba  : 1 match
              Python : No match
"""

result = re.findall('t$',str) #['t']
result = re.findall('saat$',str) #['saat']
result = re.findall('saatt$',str) # []

"""
    * - Bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder.

        ma*n => mn      : 1 match
                man     : 1 match
                maaan   : 1 match
                main    : No matct(a'nın arkasına n gelmiyor)
"""

result = re.findall('sa*t',str) # ['saat']
result = re.findall('sa*kt',str) #[]

"""
    + - Bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder.

        ma+n => mn      : No match
                man     : 1 match
                maaan   : 1 match
                main    : No matct(a'nın arkasına n gelmiyor)
"""

result = re.findall('sa*t',str) # ['saat']

"""
    ? - Bir karakterin sıfır  ya da bir kez olmasını kontrol eder.

        ma?n => mn      : No match
                man     : 1 match
                maaan   : 1 match
                main    : No matct(a'nın arkasına n gelmiyor)
"""

result = re.findall('sa?t',str) # []

"""
    {} - Karaktr sayısını kontrol eder.

        al{2}       => a karakterinin arkasına l karakteri 2 kez tekrarlanmalı
        al{2,3}     => a karakterinin arkasına l karakteri en az 2 kez en fazla 3 kez tekrarlanmalı
        [0-9]{2,4}  => en az 2 en çok 4 basamaklı sayılar.
"""

result = re.findall('a{2}',str) #['aa']
result = re.findall('[0-9]{2}',str) # ['40']

"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir

        a|b     => a ya da b
                    
            cde    => no match
            ade    => 1 match
            acdbea => 3 match

"""

"""
    () - gruplamak için kullanılır.

        (a|b|c)xz => a,b,c karakterlerini arkasına xz gelmelidir.

"""

"""
    \ - Özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterini arar.Yani $ regular eexp engine tarafından yorumlanmaz

    \A - Belirtilen karaktr string in başında mı ?
        \Athe => thee string in başında mı ?
    
    \Z - Belirtilen karaktr string in sonunda mı ?
        the\Z => the string in sonunda mı ? 
    
    \b - Belirtilen karaktr kelimenin başında veya sonunda mı ?
        \bthe => the kelimenin başında mı ?
        the\b => the kelimenin sonunda mı ? 
    

"""

print(result)