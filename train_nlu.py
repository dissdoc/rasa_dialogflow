from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer


if __name__ == '__main__':
    training_data = load_data('data/data.md')
    trainer = Trainer(config.load('nlu_config.yml'))

    trainer.train(training_data)
    trainer.persist('models/nlu', fixed_model_name='current')
