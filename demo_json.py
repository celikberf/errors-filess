import json
import os

class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email


class UserRepostory:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json','r',encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    user  =  json.loads(user)
                    newUser = User(username=user['username'],password=user['password'], email=user['email'])
                    self.users.append(newUser)
            print(self.users)

    def  register(self, user: User):
        self.users.append(user)
        self.saveToFile()
        print('Kullanıcı oluşturuldu')

    def login(self,username,password):
        
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('Login yapıldı...')
                break

    def logout(self):
            self.isLoggedIn = False
            self.currentUser = {}
            print('Çıkış yapıldı...')
        
    def identity(self):
            if self.isLoggedIn:
                print(f'username: {self.currentUser}')
            else:
                print('giriş yapılmadı...')

    def saveToFile(self):

        list = []
        for user  in self.users:
            list.append(json.dumps(user.__dict__))
    
        with open('users.json','w') as  file:
            json.dump(list,file)

repostory = UserRepostory()

while True:
    print('Menü'.center(50,'*'))
    secim = input('1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nSeçiminiz: ')
    if secim == '5':
        break
    else:
        if secim == '1':
            username  = input('username : ')
            password  = input('password : ')
            email  = input('email : ')

            user = User(username = username , password = password , email = email)
            repostory.register(user)

            print(repostory.users)

        elif secim == '2':
            if repostory.isLoggedIn:
                print('zaten login oldunuz')
            else:
                username = input('username : ')
                password = input('password : ')

                repostory.login(username,password)

        elif secim == '3':
            repostory.logout()
        
        elif secim == '4':
            repostory.identity()

        else:
            print('YANLIŞ SEÇİM!')