#Jonathan Mai
#Tutorial 1
import random

#Task 1
print('Task 1')
print('Hello World')
input()

#Task 2
print('Task 2')
user_guess = input('Please enter an integer: ')
print(user_guess)
input()

#Task 3
print('Task 3')
user_guess = int(user_guess)
converted_user_guess = int(user_guess)
print(user_guess * 3)
print(converted_user_guess * 3)
user_guess = str(user_guess)
print(user_guess * 3)
print("I entered " + user_guess)
#print("I entered " + converted_user_guess)

input()

#Task 4
print('Task 4')
#print(random.randint(1,20))
for i in range (1,21,1):
    #print(i % 2)
    if (i % 2) == 0:
        print('even')
    elif i == 7:
        print('Snowflake')
    else:
        print('odd')

#Task 5
print('Task 5')
user_input = input('Please enter an integer greater than 13: ')
converted_user_input = int(user_input)
for i in range (1,converted_user_input,1):
    if (i % 2) == 0:
        print('even')
    elif i == 7:
        print('Lucky')
    elif i == 13:
        print('Unucky')
    else:
        print('odd')

#Task 6
print('Task 6')
while True:
    lastname_input = input('Hey! What is your last name? (Mai): ')
    if lastname_input == 'Mai':
        print('Hello, Mai! Have a good day!')
        break
    else:
        print('Hello, ' + lastname_input + '! We are waiting for Mai!')

#Task 7
print('Task 7')
counter = 0
while counter < 10:
    print(counter)
    counter = counter + 1

#Task 8
print('Task 8')
for i in range(0,5):
    random_Number = random.randint(-10,10)
    print(random_Number, end=" ")
    
print()
print()
print('Press Enter to end the script')
input()















