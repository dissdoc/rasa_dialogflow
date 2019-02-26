from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


class ActionPersonName(Action):
    def name(self):
        return 'action_person_name'

    def run(self, dispatcher, tracker, domain):
        person = tracker.get_slot('person')
        print(person)
        dispatcher.utter_message('Test message from action...')

        return [SlotSet('person', 'Mr. ' + person)]


class ActionPriceOfFender(Action):
    def name(self):
        return 'action_price_fender'

    def run(self, dispatcher, tracker, domain):
        fender = tracker.get_slot('kind_guitar')

        dispatcher.utter_message('db connected emulation')
        dispatcher.utter_message('... checking {} list...'.format(fender))

        return [SlotSet('no_matches', 'squier')]


class ActionPriceOfGibson(Action):
    def name(self):
        return 'action_price_gibson'

    def run(self, dispatcher, tracker, domain):
        gibson = tracker.get_slot('kind_guitar')

        dispatcher.utter_message('... find {}...'.format(gibson))

        return [SlotSet('price', '$780')]
