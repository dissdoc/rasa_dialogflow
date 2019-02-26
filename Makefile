help:
	@echo " Demo Stand to Show NLU "

run:
	make run-actions&
	make run-core

run-core:
	python -m rasa_core.run --core models/dialogue --endpoints endpoints.yml

run-actions:
	python -m rasa_core_sdk.endpoint --actions actions

train-nlu:
	python train_nlu.py

train-dialogue:
	python train_dialogue.py

run-console:
	python -m rasa_core.run -d models/dialogue -u models/nlu/default/current

visualize:
	python visualize.py
