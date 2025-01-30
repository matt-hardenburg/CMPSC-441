#Poker Dice Challenge - www.101computing.net/fancy-a-game-of-poker-dice/
from random import randint

def isEven(number):
    return number % 2 == 0

def isOdd(number):
    return number % 2 == 1

#My Program starts here    
dice1=randint(1,6)
dice2=randint(1,6)
dice3=randint(1,6)
print("############################ Poker Dice ############################")
print("                         ### The Rules ###")
print("In this game you will throw 3 dice")
print("If all dice are equal (three of a kind) your score will go up by 50 points")
print("If you have a pair (2 dice of the same value) your score will go up by 10 points")
print("If you have a straight (3 consecutives dice such as 2,3,4) your score will go up by 30 points")
print("If all 3 dice are displaying odd numbers your score will go up by 15 points")
print("If all 3 dice are displaying even numbers your score will go up by 15 points")
print("############################ Ready? ############################")

print("Dice 1: " + str(dice1))
print("Dice 2: " + str(dice2))
print("Dice 3: " + str(dice3))

score=0
#Check if we have 3 even numbers
if isEven(dice1)==True and isEven(dice2)==True and isEven(dice3)==True:
    print("3 Even Numbers!")
    score = score + 15

#Check if we have 3 odd numbers
if isOdd(dice1)==True and isOdd(dice2)==True and isOdd(dice3)==True:
    print("3 Odd Numbers!")
    score = score + 15

#Check if we have 3 of a kind
if dice1 == dice2 and dice2 == dice3:
    print("Three Of A Kind!")
    score += 50

#Check if we have a pair
if dice1 == dice2 or dice1 == dice3 or dice2 == dice3:
    print("Two Of A Kind!")
    score += 10

#Check if we have a straight
sorted = [dice1, dice2, dice3]
sorted.sort()
if sorted[0] == (sorted[1] - 1) and sorted[1] == (sorted[2] - 1):
    print("Straight!")
    score += 30


#Display Final Score:
print("Your Score is: " + str(score))




    
