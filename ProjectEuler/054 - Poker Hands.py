""" ---------------------------------
Suits:
0 - clubs
1 - diamondss
2 - hearts
3 - spades

Ranks:
0 - nothing (highest card)
1 - pair
2 - two pair
3 - three of a kind
4 - straight
5 - flush
6 - full house
7 - four of a kind
8 - straight flush
9 - royal flush

example score:  10906050500 --> pair of seven hearts
rank    1
hand    09
        06
        05
        05
        00
-------------------------------------
""" 
cards = {'2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, 'T':8, 'J':9, 'Q':10, 'K':11, 'A':12}
suits = {'C':0, 'D':1, 'H':2, 'S':3}


def score(hand):
    #split hand into nums and suits
    hand.sort()
    nums = []
    soots = []
    for card in hand:
        nums.append(card[0])
        soots.append(card[1])


    #check for same suit
    flush = False
    fail = False
    for i in range(4):
        if soots[i+1] != soots[0]:
            fail = True
            break
    if not fail:
        #check for royal flush
        if nums == [8, 9, 10, 11, 12]:
            input("royal flush")
            return 90000000000 + ((nums[4]*100000000)+(nums[3]*1000000)+(nums[2]*10000)+(nums[1]*100)+nums[0])
        #check for straight flush
        fail1 = False
        for i in range(4):
            if nums[i] != nums[i+1] - 1:
                fail1 = True
                break
        if not fail1:
            input("straight flush")
            return 80000000000 + ((nums[4]*100000000)+(nums[3]*1000000)+(nums[2]*10000)+(nums[1]*100)+nums[0])
        flush = True

    #check for 4 of a kind
    if nums[1] == nums[2] and nums[2] == nums[3] and (nums[0] == nums[1] or nums[4] == nums[1]):
        input("4oak")
        return 70000000000 + ((nums[4]*100000000)+(nums[3]*1000000)+(nums[2]*10000)+(nums[1]*100)+nums[0])

    #check for full house
    if nums[0] == nums[1] and nums[3] == nums[4] and (nums[2] == nums[1] or nums[2] == nums[3]):
        #input("full house")
        return 60000000000 + ((nums[4]*100000000)+(nums[3]*1000000)+(nums[2]*10000)+(nums[1]*100)+nums[0])

    #if flush (we already checked)
    if flush:
        #input("flush")
        return 50000000000 + ((nums[4]*100000000)+(nums[3]*1000000)+(nums[2]*10000)+(nums[1]*100)+nums[0])

    #check for straight
    fail = False
    for i in range(4):
        if nums[i] != nums[i+1] - 1:
            fail = True
            break
    if not fail:
        #input("straight")
        return 40000000000 + ((nums[4]*100000000)+(nums[3]*1000000)+(nums[2]*10000)+(nums[1]*100)+nums[0])
    
    #check for three of a kind
    if (nums[0] == nums[1] and nums[1] == nums[2]) or (nums[1] == nums[2] and nums[2] == nums[3]) or (nums[2] == nums[3] and nums[3] == nums[4]):
        #input("3oak")
        return 30000000000 + ((nums[4]*100000000)+(nums[3]*1000000)+(nums[2]*10000)+(nums[1]*100)+nums[0])

    #check for pair
    checked = []
    pair = -1
    for num in nums:
        if num in checked:
            if pair == -1:
                pair = num
            else:
                #two pairs
                return 20000000000 + ((nums[4]*100000000)+(nums[3]*1000000)+(nums[2]*10000)+(nums[1]*100)+nums[0])
        checked.append(num)
    #if pair
    if pair != -1:
        nums.remove(pair)
        return 10000000000 + ((pair*100000000)+(nums[2]*10000)+(nums[1]*100)+nums[0])
    
    #nothing (highest card)
    return ((nums[4]*100000000)+(nums[3]*1000000)+(nums[2]*10000)+(nums[1]*100)+nums[0])


def pokerHands(filename:str):

    #read file
    with open(filename, 'r') as file:
        hands = file.readlines()
        file.close()

    #play each hand
    s = -1 # <--- dont ask me why
    for hand in hands:

        #parse hands
        hand1 = [[cards[hand[0]],suits[hand[1]]], [cards[hand[3]],suits[hand[4]]], [cards[hand[6]],suits[hand[7]]], [cards[hand[9]],suits[hand[10]]], [cards[hand[12]],suits[hand[13]]]]
        hand2 = [[cards[hand[15]],suits[hand[16]]], [cards[hand[18]],suits[hand[19]]], [cards[hand[21]],suits[hand[22]]], [cards[hand[24]],suits[hand[25]]], [cards[hand[27]],suits[hand[28]]]]
        
        #score hands
        if score(hand1) > score(hand2):
            s += 1

    return s

print(pokerHands("054 - poker.txt"))