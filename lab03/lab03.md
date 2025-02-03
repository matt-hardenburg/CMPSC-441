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
>The agent has generated a new starting point within the same general setting provided originally.  The agent never asked for a character sheet or player stats and seems to be making them up as needed. Since the agent did not have access to a character sheet, it was expecting me to roll for it. The agent also takes a more freeformed approach to the session, almost acting as a choose-your-own-adventure with either static choices or queried choices. However, it did not necessarily have a good grasp of the mechanics of combat or balancing, throwing a level 1 rogue against 4 enemies at the same time. It also continued to modify me expertise skills as it continued generation, which is incorrect. With the smaller max token limit, the results were being generated a bit faster, but still took longer than was enjoyable for a DND session.

#### Reflection/Analysis of the result. 
>While the model is generating more unique content in a quicker timespan, the response generations still take too long to be a truly enjoyable experience. Additionally, with the current prompts, it does not follow the rules of DnD properly. Overall, the model performed better than the previous, as it produced a more creative a free-flowing session, but still suffers from response generation time. 


### Step 3
#### Intention
>I want to achieve a more creative result within a smaller amount of tokens. This should hopefully speed up response time generation.

#### Action/Change
>On the third iteration, I have changed the temperature to 2 and the max_tokens to 250. Additionally, I have added additional system level messages to further clarify the rules of the scenario.

#### Result
>The agent decided to have me control an entire party rather than my single character this iteration. The agent began the session with background and a more structured overview of the scenario than any of the previous models. However, the model does not follow its own patterns for combat. On some turns i am expected to manipulate the entire party, but on others i can only choose a predetermined action for a specific party member. Additionally, the enemy never seems to attack. The model also explains its actions as if to evidence that it is attempting to follow the rules specified by the system messages.

#### Reflection/Analysis of the result. 
>Overall, this model produced the most enjoyable session so far, primarily due to the faster response time. I believe that the temperature is too high, as it is trying to follow a strict ruleset, but keeps interpretting it in different ways. A more deterministic approach may lead to a more structured game. While decreasing the max tokens has increased the response time, the agent does sometimes produce gibberish in an attempt to stay within the limit.


### Step 
#### Intention
>I want to achieve a more deterministic result while maintaining a faster respon generation time.

#### Action/Change
>On the fourth iteration, I changed the temperature to 0 and clarified the rules regarding the scenario in the system messages.

#### Result
>The agent provided an appropriate amount of background to the session while mainting its response time. The encounter were left as open ended questions, and allowed the player to advance in a creative way. The agent also maintained adherance to its own pattern for combat encounters.

#### Reflection/Analysis of the result. 
>Overall, this agent was the best iteration produced. The encounter proceeded logically and allowed the player to make their own choices without straying from the DnD 5E ruleset. The response time remained acceptable, but could still be improved. I have noticed that the performance of the model is directly tied to the quality of the system message instructions. As the system messages become more defined, the more structured session is produced.