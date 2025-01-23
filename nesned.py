# def greeting(name):
#     print('hello ', name)

# print(greeting('berf'))
# print(greeting)

# sayHello = greeting

# print(sayHello)
# print(greeting)

# print(greeting('berf'))
# # print(sayHello('berf'))

# del sayHello # sayHello nun adresini değil tanımıını silmiş oluyoruz
# print(greeting) 

# encapsulation

# def outer(num1):
#     print('outer')
#     def innerIncrement(num1):
#         print('inner')
#         return num1 + 1
#     num2 = innerIncrement(num1)
#     print(num1,num2)
    
# outer(10)

def factorial(number):
    if not isinstance(number,int):
        raise TypeError("number must be an integer")
    if not number >= 0: 
        raise ValueError("number must be zero or possitive")

    def innerFactorial(number):
        if number <= 1:
            return 1
        
        return number * innerFactorial(number - 1)
    
    return innerFactorial(number)

try:   
    print(factorial(2))
    
except Exception as ex:
    print(ex)