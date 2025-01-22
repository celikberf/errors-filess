with open("newfile.txt","r") as file: #with ile file.close()  yapmamıza gerek yok
    content = file.read(10)
    print(content)
    file.seek(0) #0 a gönderir.
    print(file.tell()) #konumunu verir
    content2 = file.read()
    print(content2)

