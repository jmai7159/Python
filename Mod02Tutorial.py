#Jonathan Mai
#Mod 02 Tutorial

import random
item_list = [1, 'two', 3, 'four', 5, 'six', 7, 'eight', 9, 'ten']
new_list = []

def marvel(name):
    position = random.randint(0,9)
    item_list.insert(position, name)

static_item_list = []
counter = 0

while counter < 10:
    item = input("Please enter an item: ")
    static_item_list.append(item)
    counter = counter + 1

for i in static_item_list:
    print(i)

#Task 1
print('\nTask 1')
print("This list has 10 items: " + str(len(item_list) == 10))

#Task 2
print('\nTask 2')
print(item_list)

#Task 3
print('\nTask 3')
first_item = item_list[0]
last_item = item_list[9]
item_list[0] = last_item
item_list[9] = first_item
print(item_list)

#Task 4
print('\nTask 4')
print(str(item_list[0:3]) + " " + str(item_list[7:]))

#Task 5
print('\nTask 5')
for i in item_list:
    print(i)

#Task 6
print('\nTask 6')
if 'cat' in item_list:
    print("There is a cat in my list.")
else:
    print("There is no cat in my list.")

#Task 7
print('\nTask 7')
hero = input("I need a hero: ")
marvel(hero)
print(item_list)

#Task 8
print('\nTask 8')
print(hero + " is at index " + str(item_list.index(hero)))


#Task 9
print('\nTask 9')
for i in item_list:
    try:
        int(i)
        new_list.append(int(i))
    except:
        continue

new_list.sort()
print(new_list)

#Task 10
print('\nTask 10')
tuple_list = tuple(item_list)
print(tuple_list)

#Task 11
print('\nTask 11')
try:
    tuplelist[0] = 'cat'
except:
    print("Tuples are immutable!")

#Task 12
print('\nTask 12')
list_in_list = [[1,2,3],['a','b','c']]

for i in list_in_list:
    for j in i:
        print(j)











