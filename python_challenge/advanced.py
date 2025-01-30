#Battle of the Knights - www.101computing.net/battle-of-the-knights/
import random

def knightNameGenerator():
   #Initialise list of possible first names and nicknames
   firstnames = ["Lancelot","Charles","Henry","William","James","Richard","Edward"]
   nicknames = ["Brave","Horrific","Courageous","Terrific","Fair","Conqueror","Victorious","Glorious","Invicible"]
  
   #Randomely pick one first name and one nickname
   firstname = random.choice(firstnames)
   nickname =  random.choice(nicknames)
  
   #Use String concatenation to generate and return the full name
   return firstname + " The " + nickname 
  

class Knight:
    name = "" 
    health = 0 
    state = 0   #initialize state
    actions = []
    defending = False
    
    def __init__(self):
        self.name = knightNameGenerator()
        self.health = 100
        self.state = 1  # Battle
        self.actions = [self.attack, self.defend, self.rest]
        self.defending = False


    def pickAction(self):
        self.defending = False
        return random.choice(self.actions)
    

    def draw(animation):
        # execute specified draw animation
        pass
    

    def attack():
        # call attack animation
        pass


    def rest(self):
        # call rest animation
        self.health += random.randint(1, 9)


    def defend(self):
        # call defend animation
        self.defending = True


    def respond(self, action, is_defending):
        if action == "attack":
            if not self.defending:
                self.health -= random.randint(1, 9)


    def status(self):
        print(self.name + ": " + self.health + "health remaining")


    def isAlive(self):
        return self.health > 0

  
#Main code to test our function
#
# initialize
p1 = Knight()
print("Player 1: Your name is: " + p1.name)
p2 = Knight()
print("Player 2: Your name is: " + p2.name)

# game loop
while p1.state == 1 and p2.state == 1:
    # pick actions
    p1_choice = p1.pickAction()
    p2_choice = p2.pickAction()

    # execute actions
    p1_choice()
    p2_choice()

    # respond to opponent's action
    p1.respond(p2_choice.__name__)
    p2.respond(p2.choice.__name__)

    # report status of players
    p1.status()
    p2.status()

    # check for game over
    if not p1.isAlive() or not p2.isAlive():
        p1.state = 2
        p2.state = 2


# determine winner
if p1.health > p2.health:
    # draw p1 victory
    print(p1.name + " is victorious!")
elif p1.health < p2.health:
    # draw p2 victory
    print(p2.name + " is victorious!")
else:
    # draw tie scene
    print("It was a tie!")