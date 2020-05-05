import tkinter as tk
import random

def loadImages(cardImages):
    suits = ['heart', 'club', 'diamond', 'spade']
    faceCards = ['jack', 'queen', 'king']

    for suit in suits:              #for each suit retrives the image of the cards
        for card in range(1, 11):   #first number cards
            name = 'cards\\{0}_{1}.ppm'.format(card, suit)
            image = tk.PhotoImage(name=name)
            cardImages.append((card, image))
        
        for card in faceCards:      #ext the face cards
            name = 'cards\\{0}_{1}.ppm'.format(str(card), suit)
            image= tk.PhotoImage(name=name)
            cardImages.append((10, image))


def dealCard(frame):
    nextCard = deck.pop(0)
    tk.Label(frame, image=nextCard[1], relief='raised').pack(side='left')
    return nextCard


def score_hand(hand):
    score2 = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score2 += card_value
        #if we ge get bust check if there is an ace and subtract 10
        if score2 > 21 and ace:
            score2 -= 10
            ace = False
        return score2


def dealDealer():
    dealerHand.append(dealCard(dealerCardFrame))
    dScore = score_hand(dealerHand)
    dealerScore.set(dScore)

    player_score = score_hand(playerHand)
    if player_score > 21:
        resultText.setvar('Dealer wins!')
    elif dScore > 21 or dScore < player_score:
        resultText.setvar('Player Wins!')
    elif dScore > player_score:
        resultText.setvar('Dealer wins!')
    else:
        resultText.setvar('Draw!')


def dealPlayer():
    playerHand.append(dealCard(playerCardFrame))
    score = score_hand(playerHand)
    
    PlayerScore.set(score)
    if score > 21:
        resultText.setvar('dealer wins!')
    # global score
    # global playerAce
    # cardValue = dealCard(playerCardFrame)[0]
    # if cardValue == 1 and not playerAce:
    #     cardValue = 11
    # score += cardValue
    # if score > 21  and playerAce:
    #     score -= 10
    # PlayerScore.set(score) 
    # if score > 21:
    #     result.set('Dealer wins')
    # dealCard(playerCardFrame)
    print(locals())

mainW = tk.Tk()

mainW.title('Black Jack')
mainW.geometry('640x480+200+100')
mainW.config(bg='green')

#________result_______#
result = tk.StringVar()
resultText = tk.Label(mainW, textvariable=result)
resultText.grid(row=0, column=0, columnspan=3, sticky='e')

#________________Card Frame___________________#
cardFrame = tk.Frame(mainW, relief='sunken', borderwidth=1, bg='green')
cardFrame.grid(row=1, column=0, rowspan=2, columnspan=3, sticky='ew')
#_____dealer score______#
dealerScore = tk.IntVar()
tk.Label(cardFrame, text='Dealer', bg='green', fg='red').grid(row=0, column=0)
tk.Label(cardFrame, textvariable=dealerScore, bg='green', fg='white').grid(row=1, column=0)
#_____Player score______#
PlayerScore = tk.IntVar()
tk.Label(cardFrame, text='Player', bg='green', fg='red').grid(row=2, column=0)
tk.Label(cardFrame, textvariable=PlayerScore, bg='green', fg='white').grid(row=3, column=0)

#______Dealer card frame_________#
dealerCardFrame = tk.Frame(cardFrame, bg='green')
dealerCardFrame.grid(row=0, column=1, sticky='ew', rowspan=2)
#______Player cards Frame________#
playerCardFrame = tk.Frame(cardFrame, bg='green')
playerCardFrame.grid(row=2, column=1, sticky='ew', rowspan=2)

#_________Buttons_________#
buttonFrame = tk.Frame(mainW)                                           #Button Frame
buttonFrame.grid(row=5, column=0, columnspan=3, sticky='w')
dealerButton = tk.Button(buttonFrame, text='Dealer', command=dealDealer)#Dealer Button
dealerButton.grid(row=0, column=0, sticky='w')
playerButton = tk.Button(buttonFrame, text='Player', command=dealPlayer)#player Button
playerButton.grid(row=0, column=1)

#______load cards_______#
cards = []
loadImages(cards)

#create a new deck of cards & shuffle them
deck = list(cards)
random.shuffle(deck)

#creating a list to store player & dealer hand
dealerHand = []
playerHand = []

dealPlayer()
dealerHand.append(dealCard(dealerCardFrame))
dealPlayer()

mainW.mainloop()