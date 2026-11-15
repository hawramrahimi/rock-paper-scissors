#کتاب خانه رندوم
import random

#لیست سنگ کاغذ و قیچی
game = ['stone' , 'paper' , 'scissors']

#گرفتن سنگ کاغذ یا قیچی از کاربر
h = input('stone - paper - scissors : ')

#انتخاب رندم سنگ کاغذ یا قیچی
r = random.choice(game)
print(r)

#برسی کردن برنده
if h == 'stone' and r == 'stone':
    print('equal')
elif h == 'stone' and r == 'paper':
    print('you lost')
elif h == 'stone' and r == 'scissors':
    print('you won')
elif h == 'paper' and r == 'stone':
    print('you won')
elif h == 'paper' and r == 'paper':
    print('equal')
elif h == 'paper' and r == 'scissors':
    print('you lost')
elif h == 'scissors' and r == 'stone':
    print('you lost')
elif h == 'scissors' and r == 'paper':
    print('you won')
elif h == 'scissors' and r == 'scissors':
    print('equal')
else :
    print('error')
     