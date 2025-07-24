# operator in python with meaning
# == is equal to
# != is not equal to 
# < is less then
# > is greater then 
# <= is less then or equal to
# >= is greater then or equal to

# flow control
name = input('enter your name:')
if name == 'razin':
    print('hello razin')
password = input('enter your password:')
if password == 'khan':
    print('Access granted')
else:
    print('wrong password')

age = int(input('enter your age:'))
if age == 12:
    print('your age is correct')
elif age < 12:
    print('you are not razin! you are litte heacker.pls stop trying!')
elif age > 200:
    print('Unlike you,Razin is not an undead, immortal vampire')  
elif age > 100:
    print('you are not razin,grannie.')


spam = int(input('enter a number:'))
if spam < 5:
    print('hello, wrold')
    spam = spam + 1
print(spam)

# while loop 
name = input('enter your name:')
while name != 'razin':
    print('pls enter your name')
    name = input('now enter the correct name of you:')
    if name == 'khan':
        break
print('thanks ' + name)

# Trapped in an infinite loop?
while True:
    print('you are trapped in python!')
