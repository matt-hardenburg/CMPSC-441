from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Matthew Hardenburg'
model = 'llama3.2'
options = {
  'temperature': 0, # deterministic (0) -> creative (2), default is 1
  'max_tokens': 250, # response length
}
messages = [
  {'role': 'system', 'content': 'You are a dungeons and dragons dungeon master. You should always respond as a DM.'},
  {'role': 'system', 'content': 'Follow the DND 5E ruleset.'},
  {'role': 'system', 'content': 'The setting of the adventure should be a crypt filled with various undead monsters and treasure.'},
  {'role': 'system', 'content': 'This is a level 1 adventure.'},
  {'role': 'system', 'content': 'The party consists of only a level 1 rogue hunting for treasures in an abandoned crypt.'},
  {'role': 'user', 'content': "Begin the session."}
]
# But before here.

options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:
  response = chat(model=model, messages=messages, stream=False, options=options)
  # Add your code below
  print(f'DM: {response.message.content}')
  messages.append({'role': 'assistant', 'content': response.message.content}) # store model response
  message = {'role': 'user', 'content': input('You: ')}
  messages.append(message) # store user response
  # But before here.
  if messages[-1]['content'] == '/exit':
    break

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)

