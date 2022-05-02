from greetings import greets
from translate import Translator

translator = Translator(to_lang='pl')

for g in greets:
    print(translator.translate(g).title())