#US Presidents Quiz - www.101computing.net/US-Presidents-Quiz/
import random

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("x       US Presidents       x")
print("x          Quiz             x")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("")

file = open("./us-presidents.csv")
#Stores all the content of the text file into a list
listOfPresidents = file.readlines()
file.close()

#Pick a "line" from the list, at random
# line = random.choice(listOfPresidents)

# #Split the fields
# president1=line.split(",")

#Access each field
# print(president1[0])
# print(president1[1])
# print(president1[2])
# print(president1[3])

#Complete the code here
score = 0
incorrect = False

while score < 10 and not incorrect:
    is_pres1 = False

    line = random.choice(listOfPresidents)
    president1 = line.split(",")

    line = random.choice(listOfPresidents)
    president2 = line.split(",")

    print("\nWho was the most recent President?")
    print("A) " + str(president1[1]))
    print("B) " + str(president2[1]))
    print("C) Clue")
    
    user_input = input().upper()
    while (user_input != "A" and user_input != "B") or user_input == "C":
        if not user_input == "C": 
            print("Invalid input, try again")
        else:
            print(str(president1[1]) + " start: " + str(president1[2]) + " " + str(president1[1] + " end: " + str(president1[3])))
            print(str(president2[1]) + " start: " + str(president2[2]) + " " + str(president2[1] + " end: " + str(president2[3])))

        user_input = input().upper()

    is_pres1 = int(president1[0]) > int(president2[0])

    if (user_input == "A" and is_pres1) or (user_input == "B" and not is_pres1):
        print("Correct!")
        score += 1

        if score == 10:
            print("You win!")

    else:
        print("Incorrect!")
        incorrect = True
        