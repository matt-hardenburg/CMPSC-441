# Prompt Engineering Process

### Step 1
#### Intention
>This is the first iteration of the agent using llama3.2 with temperature=0.5 and max_tokens=1000.

#### Action/Change
>The agent will create an adventure in a crypt filled with undead and treasure.

#### Result
>The agent successfully began an adventure in the specified setting. It prompts me to roll for actions as needed, and provides pathways to follow. It's unknown however if any of these paths are actually connected or just generated on the spot. It takes a decently long time to return a response (30 seconds). I ended the session early before it's resolution to attempt to fine-tune the model.

#### Reflection/Analysis of the result. 
>The llama3.2 model worked decently well out of the box. However, there was no structure to the dungeon and it felt like each room was generated procedurally with barely any connection. Additionally, the model took a decent chunk of time generating each response. This may be due to the hardware of the lab machine, but the model will need to be fine tuned to find out. 1000 as the value for max tokens may be too much. It allows for a good amount of worldbuilding and setting description, but may be too much for the model to generate in quick succession.


### Step 2
#### Intention
>This is the second iteration of the agent using llama3.2 with temperature=1 and max_tokens=500

#### Action/Change
>The change to the temperature will hopefully allow the model to be more creative in creating the dungeon when following the same prompt as the previous iteration. Additionally, a smaller max_tokens value may help the model generate responses in a more timely manner, i.e. generate less more often. 

#### Result
> The agent has generated a new starting point within the same general setting provided originally.  The agent never asked for a character sheet or player stats and seems to be making them up as needed. The agent also did not care that I was a rogue casting a ninth level magic missile. The game also did not know what that was and made up the damage of the spell.

#### Reflection/Analysis of the result. 
>While the model is generating more unique content in a quicker timespan, the response generations still take too long to be a truly enjoyable experience. Additionally, with the current prompts, it does not follow the rules of DnD properly.
