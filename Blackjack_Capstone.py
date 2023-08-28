import random

instructions = 'How to play Blackjack:\n\nIn each game of Blackjack, you are against the dealer and your goal is to ' \
               'draw cards that add up to the highest number possible without going over 21.\nYou can draw 13 cards,' \
               'with the name of the card being how many points it\'s worth, Jack, King and Queen being worth 10 and' \
               ' an Ace being worth 1 or 11 \ndepending on what you choose or whichever one won\'t make you lose ' \
               'instantly. You will always start drawing first and you will draw 2 cards, if your\ntotal isn\'t ' \
               'already 21, you can choose to hit and carry on taking cards or stand. Every time you hit, the dealer' \
               ' takes another card as well and whoever\ngets above 21 loses. This is called a bust and remember, if ' \
               'you draw above 21 first, you will lose. If you choose to stand, the dealer will keep on taking\ncards ' \
               'if their score is 16 or below or until he busts. Once turns end, whoever has the highest total with ' \
               'their cards will win. You start off with £1000\nand you bet in £100 intervals. If you win, you double' \
               'your bet, if you draw you get your bet back and if you lose , you lose your bet. If you have no ' \
               'money\nleft, you lose. This game was created by Safwan\n'

cards = {'Ace': [1, 11], 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
'Ten': 10, 'Jack': 10, 'King' : 10, 'Queen': 10}


def draw_card(sum):

    card = random.choice(list(cards))
    value = 0
    if card == 'Ace' and sum < 11:
        ask = input('You drew an Ace, do you choose 1 or 11? ').lower().replace(' ', '')
        while ask not in '11':
            ask = input('Please type either 1 or 11 numerically:  ').lower().replace(' ', '')
        if ask == '1':
            sum += 1
        else:
            sum += 11
    elif card == 'Ace':
        sum += 1
    else:
        value = cards[card]
        sum += value
    return sum, value, card

def opponent_draw(sum):

    card = random.choice(list(cards))
    value = 0
    if card == 'Ace' and sum < 11:
        value = random.choice([1, 11])
        sum += value
    elif card == 'Ace':
        sum += 1
    else:
        value = cards[card]
        sum += value
    return sum, value, card


def play():
    endGame = False
    playerSum = 0
    opponentSum = 0
    draws = 2
    while not endGame:
        for i in range(draws):
            draws = 1
            playerSum, value, card = draw_card(playerSum)
            if card[0] in 'AEIOU':
                print(f'You drew an {card}, your total is now {playerSum} ')
            else:
                print(f'You drew a {card}, your total is now {playerSum} ')

        if playerSum > 21:
            print('Bust! Dealer Wins')
            return playerSum, opponentSum

        # Opponent's turn
        opponentSum, value, card = opponent_draw(opponentSum)
        if card[0] in 'AEIOU':
            print(f'Opponent drew an {card}, their total is now {opponentSum} ')
        else:
            print(f'Opponent drew a {card}, their total is now {opponentSum} ')
        if opponentSum > 21:
            print('Bust! You win')
            return playerSum, opponentSum

        carryOn = input('Type H to hit or S to stand: ').lower().replace(' ', '')
        while carryOn not in 'hs':
            carryOn = input('Please type either H to hit or S to stand: ').lower().replace(' ', '')
        if carryOn == 'h':
            endGame = False
        else:
            endGame = True
    while opponentSum < 17:
        opponentSum, value, card = opponent_draw(opponentSum)
        print(f'Opponent drew a {card}, their total is now {opponentSum} ')
    if opponentSum > 21:
        print('Bust! You win')
    return playerSum, opponentSum


def score(playerSum, opponentSum, bet):
    if playerSum > opponentSum and playerSum < 22:
        print(f'You won £{bet}\n')
        return bet
    elif playerSum > opponentSum:
        print(f'You lost £{bet}\n')
        return -bet
    elif opponentSum > playerSum and opponentSum < 22:
        print(f'You lost {bet}\n')
        return -bet
    elif opponentSum > playerSum:
        print(f'You won £{bet}\n')
        return bet

    else:
        print('Push! you drew and won nothing\n')
        return int(0)

withdraw = False
balance = 1000
valid = False
print('Welcome to Blackjack!\n')
ask = input('Press H for how to play or anything else to continue\n').lower().replace(' ','')
if ask == 'h':
    print(instructions)

name = input('Enter your name: ')
print(f'You have £{balance}')
while not withdraw:
    while True:
        betStr = (input(f'How much you do want to bet? Choose in £100 intervals: £').replace(' ', ''))
        if betStr.isdigit():
            bet = int(betStr)
            if bet % 100 == 0:
                if bet <= balance:
                    break
                else:
                    print(f'You only have £{balance}')
            else:
                print('Bet has to be in £100 intervals')
        else:
            print('Give a whole number: ')
    print(f'\n{name} starts by drawing 2 cards: \n')
    playerSum, opponentSum = play()
    balance += score(playerSum, opponentSum, bet)
    print(f'You now have £{balance}')
    if balance == 0:
        print(f'You have nothing left {name}, better luck next time!\n')
        break
    end = input('Play again? Type y for yes, n for no: ')
    while end not in 'yn':
        end = input('Please type either y for yes or n for no: ')
    if end == 'n':
        withdraw = True
        print(f'Congrats {name}, you walked away with £{balance}!')
input('Enter any key to end the programme: ')
