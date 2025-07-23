# this py file says hello and ask for my name

print('hello in python world!') # hello in python world
print('what is your name?') # ask for name
myname = str(input()) #input my name as a str
print('it is good to meet you, ' + myname)
print('the length of your name is: ' + str(len(myname))) # length of my name

print('what is your age?') # ask my age
myAge = int(input()) # input my age as a int
print ('you wil be ' + str(int(myAge) + 1) + ' in a year.')