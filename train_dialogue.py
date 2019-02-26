from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy


if __name__ == '__main__':
    agent = Agent('domain.yml', policies=[MemoizationPolicy(max_history=3), KerasPolicy()])
    training_data = agent.load_data('data/stories.md')

    agent.train(training_data)
    agent.persist('models/dialogue')
