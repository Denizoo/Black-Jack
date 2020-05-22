#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import time

# function for each input
# I added two types of function when you ask for an integer, the case of an Ace taking the value of 1 or 11
# and other cases when you ask for integers (bets, number of players, etc.)
def main():
    def slow_mo(self):
        for characters in self:
            print(characters, end='')
            time.sleep(0.01)
        
    def slow_mo_list(self):
        for i in range(0, len(self)):
            for characters in self[i]:
                print(characters, end='')
                time.sleep(0.01)
            print(' ')

    # function for each input 
    # I added two types of function when you ask for an integer, the case of an Ace taking the value of 1 or 11
    # and other cases when you ask for integers (bets, number of players, etc.)
    class initiating_an_input:
        def limit_the_input(self, upper_limit, lower_limit, type_ask):
            while True:
                try:
                    if type_ask == 1:
                        k = int(input('Insert a number (min %s, max %s): ' %(lower_limit, upper_limit)))
                        if lower_limit <= k <= upper_limit:
                            return k
                            break
                        elif k > upper_limit:
                            slow_mo('You inserted a number that is too high , please insert a number between %s and %s' %(lower_limit, upper_limit))
                        elif k < lower_limit:
                            slow_mo('You inserted a number that is too low, please insert a number between %s and %s' %(lower_limit, upper_limit))
                    if type_ask ==2:
                        k = int(input('Insert either %s or %s: ' %(lower_limit, upper_limit)))
                        if lower_limit == k:
                            return k
                            break
                        if upper_limit == k: 
                            return k
                            break
                        else:
                            slow_mo("Please insert either %s or %s" %(lower_limit, upper_limit))
                except ValueError:
                    slow_mo('Please enter an integer!')
        def string_as_input(self, answer_type1, answer_type2):
            while True:
                try:
                    m = input('Insert %s or %s only: ' %(answer_type1, answer_type2)).lower()
                    if m == answer_type1:
                        return m
                        break
                    elif m == answer_type2:
                        return m
                        break
                    else:
                        slow_mo('Please insert %s or %s only: ' %(answer_type1, answer_type2))
                except ValueError:
                    pass


    # informations about the game 
    slow_mo('Before starting to play, tell us whether you want to learn more about the BlackJack game')
    first_question = initiating_an_input().string_as_input('yes', 'no')
    if first_question == 'yes':
        slow_mo('Here are the rules: At first, you will have to bet and you will receive two cards. \n The sum of those two must always remain lower or equal to 21. If you have a 21 out of the first two cards, \n you instantly win two times and a half your bet, if not you will be asked whether you want an additional card. Then comes the turn of the dealer. \n If the sum of his/her cards exceed yours and is under or equal 21, he/she wins. \n If not, you win and receive your bet twice. \n Please note that the Ace can either take the value of 1 or 11. \n The heads always take the value of 10. \n Please note that the decks will be of 52 cards that will be shuffled and distributed to the players from the left to the right! \n Have fun!')
    elif first_question == 'no':
        slow_mo("Great! Now you will have to decide with how many decks you will want to play with! \n")
    time.sleep(1)

    # number of decks you would want to play with
    number_of_decks = initiating_an_input().limit_the_input(4,1,1)
    if number_of_decks > 1:
        slow_mo('you decided to play with %s decks \n' %number_of_decks)
    if number_of_decks == 1:
        slow_mo('You decided to play with only one deck \n')
    time.sleep(1)

    # we use str(i) in order to make sure that those numbers added are a string 
    # as we want our deck to print for example '2 of Hearts' we need both to be strings
    # the player can decide how many decks he wants to play with 

    class creation_of_decks:
        def deck_of_cards(self, number_of_decks):
            d = []
            deck = []
            suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
            heads = ['Ace', 'Jack', 'Queen', 'King']
            for i in range(2,11):
                deck.append(str(i))
            for j in range(0,4):
                deck.append(heads[j])     
            for h in range(0,4):
                for g in range(0,13):
                    card_specific = (deck[g] + ' of ' + suits[h]) 
                    d.append(card_specific)
            e = number_of_decks * d
            return e

    decks = creation_of_decks().deck_of_cards(number_of_decks)
    random.shuffle(decks)

    # number of players and position in the game
    slow_mo('Please decide which table you would want to join! You will be deciding about the number of players you want to play with')
    number_of_players = initiating_an_input().limit_the_input(6,0,1)
    if number_of_players == 0:
        position_at_the_table = 0
        slow_mo('Wow, you decided to play alone against the dealer, good luck! \n it is time to decide how much you want to bet!')
    if number_of_players > 0:
        slow_mo('You will join a table with %s players \n' %number_of_players)
        slow_mo('Now, you will decide where you want to sit at the table')
        position_at_the_table = initiating_an_input().limit_the_input((number_of_players+1),1,1)
        if position_at_the_table == 1:
            slow_mo('You will be the %s st receiving your cards \n it is time to decide how much you want to bet!' %position_at_the_table)
        if position_at_the_table == 2:
            slow_mo('You will be the %s nd receiving your cards \n it is time to decide how much you want to bet!' %position_at_the_table)
        if position_at_the_table == 3:
            slow_mo('You will be the %s rd receiving your cards \n it is time to decide how much you want to bet!' %position_at_the_table)
        if position_at_the_table > 3:
            slow_mo('You will be the %s th receiving your cards \n it is time to decide how much you want to bet!' %position_at_the_table)    
    time.sleep(1)

    # Bets
    bet = initiating_an_input().limit_the_input(10000,5,1)
    slow_mo('You decided to bet %s, now you cannot withdraw your money anymore, good luck! \n' %bet)
    slow_mo('All right, lets start the game! \n')
    time.sleep(1)

    # dictionary to sum up the cards 
    # function for the sum of cards
    # turn_number starts at 0 !!!
    dict_with_ints = {'Jack of Hearts':10, 'Jack of Diamonds':10, 'Jack of Clubs':10, 'Jack of Spades':10, 'Queen of Hearts':10, 'Queen of Diamonds':10, 'Queen of Clubs':10, 'Queen of Spades':10, 'King of Hearts':10, 'King of Diamonds':10, 'King of Clubs':10, 'King of Spades':10, '2 of Hearts':2, '2 of Diamonds':2, '2 of Clubs':2, '2 of Spades':2,'3 of Hearts':3, '3 of Diamonds':3, '3 of Clubs':3, '3 of Spades':3, '4 of Hearts':4, '4 of Diamonds':4, '4 of Clubs':4, '4 of Spades':4, '5 of Hearts':5, '5 of Diamonds':5, '5 of Clubs':5, '5 of Spades':5, '6 of Hearts':6, '6 of Diamonds':6, '6 of Clubs':6, '6 of Spades':6, '7 of Hearts':7, '7 of Diamonds':7, '7 of Clubs':7, '7 of Spades':7, '8 of Hearts':8, '8 of Diamonds':8, '8 of Clubs':8, '8 of Spades':8, '9 of Hearts':9, '9 of Diamonds':9, '9 of Clubs':9, '9 of Spades':9, '10 of Hearts':10, '10 of Diamonds':10, '10 of Clubs':10, '10 of Spades':10}

    def check_cards(self, previous_sums, player_type, turn_number):
        sum_of_cards = 0
        if turn_number == 0:
            for i in range(turn_number, len(self)):
                while True:
                    try:
                        sum_of_cards = sum_of_cards + dict_with_ints[self[i]]
                        break
                    except KeyError:
                        if player_type == 1:
                            if sum_of_cards + 11 <= 21:
                                sum_of_cards = sum_of_cards + 11
                                break
                            else:
                                sum_of_cards = sum_of_cards +1
                                break
                        if player_type == 2:
                            ask_me = initiating_an_input().limit_the_input(11,1,2) 
                            #the function can be found at the beginning of the code
                            sum_of_cards = sum_of_cards + ask_me
                            break
            return sum_of_cards
        else:
            while True:
                try:
                    sum_of_cards = previous_sums + dict_with_ints[self[turn_number]]
                    break
                except KeyError:
                    if player_type == 1:
                        if sum_of_cards + 11 <= 21:
                            sum_of_cards = previous_sums + 11
                            break
                        else:
                            sum_of_cards = previous_sums +1
                            break
                    if player_type == 2:
                            ask_me = initiating_an_input().limit_the_input(11,1,2) 
                            #the function can be found at the beginning of the code
                            sum_of_cards = previous_sums + ask_me
                            break
            if sum_of_cards > 21:
                a = 'You unfortunately lost ...'
                slow_mo(a)
            return sum_of_cards
        
    # giving cards 
    # you create 7 CPUs because the player will replace one of them
    player_cards = []
    dealer_cards = []
    cpu_1 = []
    cpu_2 = []
    cpu_3 = []
    cpu_4 = []
    cpu_5 = []
    cpu_6 = []
    cpu_7 = []

    def deal_cards(self, number_of_distribution):
        for i in range(0, number_of_distribution):
            self.append(decks[0])
            decks.pop(0)

    # number_of_players because it does not take into account the player and the dealer
    # we write number_of_players+2 and number_of_players+1 as it is non inclusive
    # the range from 0 to 2 will stop at 1 and the elif needs to be written differently 
    # as the player and the dealer cards are dealt earlier, the program will directly add the cards to them
    # if the number_of_players is superior to 0 as the condition will already be fulfilled

    if number_of_players == 0:
        z = number_of_players + 2
    elif number_of_players > 0:
        z = number_of_players + 3 
    for i in range(0, z):
        if i == position_at_the_table:
            deal_cards(player_cards,2)
            a = "Player cards: \n"
            slow_mo(a)
            slow_mo_list(player_cards)
            print('\n')
            time.sleep(1)
        elif i == z - 1:
            deal_cards(dealer_cards,2)
            a = "Dealer cards: \n", dealer_cards[0], ", the other cards will stay hidden for now \n"
            slow_mo(a) 
            time.sleep(1)
        elif number_of_players > 0:
            if i == 1:
                deal_cards(cpu_1,2)
                a = "CPU_1 cards: \n"
                slow_mo(a)
                slow_mo_list(cpu_1)
                print('\n')
                time.sleep(1)
            if i == 2:
                deal_cards(cpu_2,2)
                a = "CPU_2 cards: \n"
                slow_mo(a)
                slow_mo_list(cpu_2)
                print('\n')
                time.sleep(1)
            if i == 3:
                deal_cards(cpu_3,2) 
                a = "CPU_3 cards: \n"
                slow_mo(a)
                slow_mo_list(cpu_3)
                print('\n')
                time.sleep(1)
            if i == 4:
                deal_cards(cpu_4,2)
                a = "CPU_4 cards: \n"
                slow_mo(a)
                slow_mo_list(cpu_4)
                print('\n')
                time.sleep(1)
            if i == 5:
                deal_cards(cpu_5,2)
                a = "CPU_5 cards: \n"
                slow_mo(a)
                slow_mo_list(cpu_5)
                print('\n')
                time.sleep(1)
            if i == 6:
                deal_cards(cpu_6,2)
                a = "CPU_6 cards: \n"
                slow_mo(a)
                slow_mo_list(cpu_6)
                print('\n')
                time.sleep(1)
            if i == 7:
                deal_cards(cpu_7,2)
                a = "CPU_7 cards: \n"
                slow_mo(a)
                slow_mo_list(cpu_7)
                print('\n')
                time.sleep(1)
    
    def cpu_decisions(cards, type_1):
        if type_1 == 1:#player
            while check_cards(cards,0,1,0) < 19:
                a = 'Your hand is worth: %s \n' %check_cards(cards,0,1,0)
                slow_mo(a)
                a ="Do you want to play? \n Yes \n Fair enough\n"
                slow_mo(a)
                deal_cards(cards, 1)
            else:
                if check_cards(cards,0,1,0) > 21:
                    a = 'Your hand is worth: %s \n' %check_cards(cards,0,1,0)
                    slow_mo(a)
                    a ="You cannot play anymore \n"
                    slow_mo(a)
                    pass
                else:
                    a = 'Your hand is worth: %s \n' %check_cards(cards,0,1,0)
                    slow_mo(a)
                    a ="Do you want to play? \n No \n Fair enough\n"
                    slow_mo(a)
                    pass
        if type_1 == 2:#cpu with amateur srategy
            while check_cards(cards,0,1,0) < 21:
                a = 'Your hand is worth: %s \n' %check_cards(cards,0,1,0)
                slow_mo(a)
                a ="Do you want to play? \n Yes \n Fair enough\n"
                slow_mo(a)
                deal_cards(cards, 1)
            else:
                if check_cards(cards,0,1,0) > 21:
                    a = 'Your hand is worth: %s \n' %check_cards(cards,0,1,0)
                    slow_mo(a)
                    a ="You cannot play anymore \n"
                    slow_mo(a)
                    pass
                else:
                    a = 'Your hand is worth: %s \n' %check_cards(cards,0,1,0)
                    slow_mo(a)
                    a ="Do you want to play? \n No \n Fair enough\n"
                    slow_mo(a)
                    pass
        if type_1 == 3:#cpu with better strategy
            while check_cards(cards,0,1,0) < 18:
                a = 'Your hand is worth: %s \n' %check_cards(cards,0,1,0)
                slow_mo(a)
                a ="Do you want to play? \n Yes \n Fair enough\n"
                slow_mo(a)
                deal_cards(cards, 1)
            else:
                if check_cards(cards,0,1,0) > 21:
                    a = 'Your hand is worth: %s \n' %check_cards(cards,0,1,0)
                    slow_mo(a)
                    a ="You cannot play anymore \n"
                    slow_mo(a)
                    pass
                else:
                    a = 'Your hand is worth: %s \n' %check_cards(cards,0,1,0)
                    slow_mo(a)
                    a ="Do you want to play? \n No \n Fair enough\n"
                    slow_mo(a)
                    pass   
        if type_1 == 4: # for the dealer
            while check_cards(cards,0,1,0) < 17:
                deal_cards(cards, 1)
                slow_mo_list(cards)
            else:
                pass
  
    #splits
    def split_ask(player_cards): 
        first_card = player_cards[0]
        second_card = player_cards[1]
        if first_card[0] == second_card[0]:
            slow_mo('You have two equal cards, if you want, you can split them. If you do so, you have to double your bet(same amount for each side). Do you want to split?')
            split_question = initiating_an_input().string_as_input('yes', 'no')
           
            if split_question == 'yes':
                slow_mo('Your cards will be splitted')
            elif split_question == 'no':
                slow_mo('Your cards wont be splitted')
            return split_question
        else:
            None




    
    # 2nd turn
    a = "\n Ok, now that everyone has its card, let's play!!! \n"
    slow_mo(a)
    if number_of_players == 0:
        z = number_of_players + 2
    elif number_of_players > 0:
        z = number_of_players + 3 
    for i in range(0, z):
        if i == position_at_the_table: 
            a = "Player cards: \n"
            slow_mo(a)
            slow_mo_list(player_cards)
            print('\n')
            time.sleep(1)
            split_question = split_ask(player_cards)#initiation split question if two equal cards
            if split_question == 'yes':#split part
                hand1 = []#first left
                hand1.append(player_cards[0])
                slow_mo('Lets take a look at the left side first \n')
                slow_mo_list(hand1)
                previous_sum = 0
                turn_number = 0
                previous_sum = check_cards(hand1, previous_sum, 2, turn_number)
                slow_mo('Do you want to hit(h) or stand(s)?')
                hit_or_stand = initiating_an_input().string_as_input('h', 's')
                while hit_or_stand == 'h' and previous_sum < 22:
                    deal_cards(hand1, 1)
                    slow_mo('Your new hand on the left side is: \n')
                    slow_mo_list(hand1)
                    print('\n')
                    turn_number = turn_number + 1 
                    previous_sum = check_cards(hand1,previous_sum, 2, turn_number)
                    a = 'Your new hand is worth %s \n' %previous_sum
                    slow_mo(a)
                    if previous_sum < 22:
                        slow_mo('Hit again(h) or stand(s)? ')
                        hit_or_stand = initiating_an_input().string_as_input('h', 's')
                if hit_or_stand == 's':
                    slow_mo('You wont receive another card on the left side \n')

                hand2 = []#then right side
                hand2.append(player_cards[1])
                slow_mo('Now lets take a look at the right side \n')
                slow_mo_list(hand2)
                print('\n')
                previous_sum_1 = 0
                turn_number_1 = 0
                previous_sum_1 = check_cards(hand2 ,previous_sum_1, 2, turn_number_1)
                a = 'Your second hand is currently worth %s \n' %previous_sum_1
                slow_mo(a)
                slow_mo('Do you want to hit(h) or stand(s)?')
                hit_or_stand = initiating_an_input().string_as_input('h', 's')
                while hit_or_stand == 'h' and previous_sum_1 < 22:
                    deal_cards(hand2, 1)
                    slow_mo('Your new hand is: \n')
                    slow_mo_list(hand2)
                    print('\n')
                    turn_number_1 = turn_number_1 + 1 
                    previous_sum_1 = check_cards(hand2, previous_sum_1, 2, turn_number_1)
                    a = 'Your hand is worth %s \n' %previous_sum_1
                    slow_mo(a)
                    if previous_sum_1 < 22:
                        slow_mo('Hit again(h) or stand(s)? ')
                        hit_or_stand = initiating_an_input().string_as_input('h', 's')
                if hit_or_stand == 's':
                       slow_mo('You wont receive another card on the right side \n')

            else:#without split part
                turn_number = 0
                previous_sum = 0 
                previous_sum = check_cards(player_cards, previous_sum, 2, turn_number)
                turn_number = 1
                a = 'Your cards have a total value of %s \n' %previous_sum
                slow_mo(a)
                slow_mo('Now you can either hit(h) or stand(s).') 
                hit_or_stand = initiating_an_input().string_as_input('h', 's')
                while hit_or_stand == 'h' and previous_sum < 22:
                    deal_cards(player_cards, 1)
                    slow_mo('Your new hand is: \n')
                    slow_mo_list(player_cards)
                    print('\n')
                    turn_number = turn_number + 1
                    previous_sum = check_cards(player_cards, previous_sum, 2, turn_number)
                    a = 'Your current hand is worth %s \n' %previous_sum
                    slow_mo(a)
                    if previous_sum < 22:
                        slow_mo('Hit again(h) or stand(s)? ')
                        hit_or_stand = initiating_an_input().string_as_input('h', 's')
                if hit_or_stand == 's':
                    slow_mo('Alright you wont receive another card. \n')#player gets/loses his money after every participant on the table played.
        elif i == z - 1:
            a = "Dealer: \n"
            slow_mo(a)
            cpu_decisions(dealer_cards, 4)
            a = "Dealer cards: \n"
            slow_mo(a) 
            slow_mo_list(dealer_cards)
            print('\n')
            time.sleep(1)
        elif number_of_players > 0:
            if i == 1:
                a = "CPU_1: \n"
                slow_mo(a)
                cpu_decisions(cpu_1, 1)
                a = "CPU_1 cards: \n"
                slow_mo(a)
                slow_mo_list(cpu_1)
                print('\n')
                time.sleep(1)
            if i == 2:
                a = "CPU_2: \n"
                slow_mo(a)
                cpu_decisions(cpu_2, 2)
                a = "CPU_2 cards: \n"
                slow_mo(a)
                slow_mo_list(cpu_2)
                print('\n')
                time.sleep(1)
            if i == 3:
                a = "CPU_3: \n"
                slow_mo(a)
                cpu_decisions(cpu_3, 3)
                a = "CPU_3 cards: \n"
                slow_mo(a)
                slow_mo_list(cpu_3)
                print('\n')
                time.sleep(1)
            if i == 4:
                a = "CPU_4: \n"
                slow_mo(a)
                cpu_decisions(cpu_4, 3)
                a = "CPU_4 cards: \n"
                slow_mo(a)
                slow_mo_list(cpu_4)
                print('\n')
                time.sleep(1)
            if i == 5:
                a = "CPU_5: \n"
                slow_mo(a)
                cpu_decisions(cpu_5, 3)
                a = "CPU_5 cards: \n"
                slow_mo(a)
                slow_mo_list(cpu_5)
                print('\n')
                time.sleep(1)
            if i == 6:
                a = "CPU_6: \n"
                slow_mo(a)
                cpu_decisions(cpu_6, 2)
                a = "CPU_6 cards: \n"
                slow_mo(a)
                slow_mo_list(cpu_6)
                print('\n')
                time.sleep(1)
            if i == 7:
                a = "CPU_7: \n"
                slow_mo(a)
                cpu_decisions(cpu_7, 1)
                a = "CPU_7 cards: \n"
                slow_mo(a)
                slow_mo_list(cpu_7)
                print('\n')
                time.sleep(1)
    
    # checking the results
    def results(sum_available, dealer_cards):#bets are added in this fct
        if sum_available == 21:
            slow_mo('Yay, you got a BlackJack!!! \n')
            win = (bet * 2) + (bet / 2)
            a = 'You receive: ' + str(win)
            slow_mo(a)
        elif check_cards(dealer_cards,0,1,0) == 21:
            slow_mo('The Dealer got a BlackJack! You lose everything.\n')
        elif sum_available > check_cards(dealer_cards,0,1,0) and sum_available < 22:
            slow_mo('Yeah, you won, Congratulations!\n')
            win = bet * 2
            a = 'You receive: ' + str(win)
            slow_mo(a)
        elif sum_available == check_cards(dealer_cards,0,1,0) and sum_available < 22:
            slow_mo('You have the same value like the Dealer, nobody wins!\n')
        elif sum_available < check_cards(dealer_cards,0,1,0) and check_cards(dealer_cards,0,1,0) < 22:
            slow_mo('Sorry, but you lost, the Dealer got you!\n')
        elif sum_available > 21:
            slow_mo('Bust, you lose everything.\n')
        elif check_cards(dealer_cards, 0,1,0) > 21 and sum_available < 22:
            slow_mo('The Dealer bust, you win!\n')
            win = bet * 2
            a = 'You receive: ' + str(win)
            slow_mo(a)


                
    # the results here consider people's turn
    time.sleep(0.5)
    a = 'Now lets take a look at the results! \n'
    slow_mo(a)
    time.sleep(0.5)
    if split_question == 'yes':#results for split
        slow_mo('Result for the left side: ')
        print('\n')
        results(previous_sum, dealer_cards)
        slow_mo('Result for the right side: ')
        print('\n')
        results(previous_sum_1, dealer_cards)
    elif split_question != 'yes':#results without split
        results(previous_sum, dealer_cards)
        
    
    #play again part
    print('\n')
    slow_mo("Do you want to play again? (yes/no)")
    again = initiating_an_input().string_as_input('yes', 'no')
    while again == "yes":
        main()
    if again == "no":
        slow_mo("Thanks, it was a pleasure!")
        exit()
           
main()
