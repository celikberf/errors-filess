while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x / y)
    except Exception as ex: #genel olarak tüm hatalara bu ifadeyi kullanabiliriz
        print('yanlış bilgi girdiniz' , ex)
    else:
        break
    finally:
        print('try except sonlandı')