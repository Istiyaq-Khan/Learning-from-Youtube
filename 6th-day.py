# an equivalent while loop
print('my name is')
i = 0
while i < 5:
    print(' razin five times (' + str(i) + ')')
    i = i + 1

# the starting, stoping , and stepping argument to range()

for i in range(12, 16): # the frist argument will be where the for loop variable start and the 2nd argument will be up to, but not including, the number to stop at
    print(i)

for i in range(0, 12, 2):
    print(i)
    # so this calling range(0, 12, 2)will count from zero to eight by intervals of two

for i in range(5, -1, -1):
    print(i)
    # running a for loop to print i with range(5, -1, -1) should print from five down to zero.

