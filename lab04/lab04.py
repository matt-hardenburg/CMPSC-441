from pathlib import Path
import sys

sign = 'Matthew Hardenburg'

sys.path.append(str(Path(__file__).parents[1]))

from util.llm_utils import TemplateChat

def run_console_chat(sign, **kwargs):
    chat = TemplateChat.from_file(sign=sign, **kwargs)
    chat_generator = chat.start_chat()
    print(next(chat_generator))
    while True:
        try:
            message = chat_generator.send(input('You: '))
            print('Agent:', message)
        except StopIteration as e:
            if isinstance(e.value, tuple):
                print('Agent:', e.value[0])
                ending_match = e.value[1]
                print('Ending match:', ending_match)
            break

template_file='lab04/lab04_trader_chat.json'
lab04_params = {
    'template_file': template_file,
    'end_regex': r'ORDER(.*)DONE'
}

if __name__ ==  '__main__':
    # run lab04.py to test your template interactively
    lab04_params['inventory'] = '[\'healing potion\', \'mana potion\']'
    run_console_chat(sign, **lab04_params)