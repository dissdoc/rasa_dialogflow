from rasa_nlu.model import Interpreter

import json


def pprint(o):
    print(json.dumps(o, indent=2))


if __name__ == '__main__':
    interpeter = Interpreter.load('./models/nlu/default/current')
    pprint(interpeter.parse('order'))
