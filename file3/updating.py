# with open("newfile.txt","r+") as file:  # r+= hem okuma hem yazmayı ifade ediyor yani güncellicez
#     file.seek(20)
#     file.write("deneme")

# with open("newfile.txt","r+") as file:
#     print(file.read())


with open("newfile.txt","a") as file:
    file.write("\nGüler Celik")

