from datetime import datetime
# from datetime import date
# from datetime import time

# import datetime

simdi = datetime.now()
simdi = datetime.today() # now ile aynı sey

result = datetime.now()
result = simdi.year
result = simdi.month
result = simdi.hour
result = simdi.minute

result = datetime.ctime(simdi) # daha acıklayıcı bir bilgi
result = datetime.strftime(simdi,'%Y') # sadece yıl bilgisi aldık
result = datetime.strftime(simdi,'%D') # sadece gün bilgisi aldık
result = datetime.strftime(simdi,'%B') # sadece ay bilgisi aldık
result = datetime.strftime(simdi,'%Y %B %A') 

t = '15 April 2024 hour 10:12:30'
dt = datetime.strptime(t,' %d %B %Y hour %H:%M:%S')
dt = dt.year

print(dt)

