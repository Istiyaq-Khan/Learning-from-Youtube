#import modules
import random
for i in range(5):
    print(random.randint(1,10))

#exit by writing exit
import sys
while True:
    print('type exit to exit.')
    res = input()
    if res == 'exit':
        sys.exit()
    print('you typed '+ res + '.')