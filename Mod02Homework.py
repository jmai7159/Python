#Jonathan Mai
#Mod 02 Homework Script

import random
import copy

#Main Card Deck
card_deck = [['Ace of Spades', 'King of Spades', \
            'Queen of Spades', 'Jack of Spades', \
            '10 of Spades', '9 of Spades', \
            '8 of Spades', '7 of Spades', \
            '6 of Spades', '5 of Spades', \
            '4 of Spades', '3 of Spades', \
            '2 of Spades'], \
            ['Ace of Diamonds', 'King of Diamonds', \
            'Queen of Diamonds', 'Jack of Diamonds', \
            '10 of Diamonds', '9 of Diamonds', \
            '8 of Diamonds', '7 of Diamonds', \
            '6 of Diamonds', '5 of Diamonds', \
            '4 of Diamonds', '3 of Diamonds', \
            '2 of Diamonds'],\
            ['Ace of Clubs', 'King of Clubs', \
            'Queen of Clubs', 'Jack of Clubs', \
            '10 of Clubs', '9 of Clubs', \
            '8 of Clubs', '7 of Clubs', \
            '6 of Clubs', '5 of Clubs', \
            '4 of Clubs', '3 of Clubs', \
            '2 of Clubs'],\
            ['Ace of Hearts', 'King of Hearts', \
            'Queen of Hearts', 'Jack of Hearts', \
            '10 of Hearts', '9 of Hearts', \
            '8 of Hearts', '7 of Hearts', \
            '6 of Hearts', '5 of Hearts', \
            '4 of Hearts', '3 of Hearts', \
            '2 of Hearts']]

#Game function
def game():
    while True:
        #Exit condition
        if len(game_deck) == 0:
            print("There are no more cards in the deck.")
            break

        #Select a random suit of cards
        random_suit = random.randint(0, (len(game_deck) - 1))

        #If the suit is empty, delete the empty suit and select a new suit
        if len(game_deck[random_suit]) == 0:
            del game_deck[random_suit]
            continue

        #Select a card from the suit and print the card
        random_card = random.randint(0, (len(game_deck[random_suit]) - 1))
        print(game_deck[random_suit][random_card])

        #Delete the selected card
        del game_deck[random_suit][random_card]
        break


#Game Body
game_deck = copy.deepcopy(card_deck)
print("The deck has been shuffled.")
while True:
    #Ask for user input, if user does not input an integer, print exception and try again.
    try:
        user_draw_amount = input("How many cards would you like to draw?: ")
        draw_amount = int(user_draw_amount)    
    except:
        print("Please enter a number!")
        continue

    #Draw as many cards as the user has selected using the game function.
    for i in range(draw_amount):
        game()

    #Ask if the user wants to quit, shuffle, or continue drawing cards.
    print("Would you like to quit(q), shuffle(s), or continue drawing cards(c)?")
    user_choice = input()
    if user_choice == "q":
        break
    elif user_choice == "s":
        game_deck = copy.deepcopy(card_deck)
        continue
    elif user_choice == "c":
        continue
    else:
        print("Invalid input, by default, exit program.")
        break

#End of script.
print("Thank you for playing! Press enter to exit the script.")
input()
