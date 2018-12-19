SHELL := /bin/bash

install:
	virtualenv venv --python=python; \
	source ./venv/bin/activate; \
	pip install -r requirements.txt;

test:
	source ./venv/bin/activate; \
        cd SLCBBetterQuotes; \
	python -m pytest -v --log-cli-level=INFO ../tests/*.py -s ${ARGS};

release:
	mkdir tmp; \
	git archive -o ./tmp/SLCBBetterQuotes-git.zip HEAD; \
	mkdir tmp/SLCBBetterQuotes; \
	mv ./tmp/SLCBBetterQuotes-git.zip ./tmp/SLCBBetterQuotes/; \
	unzip ./tmp/SLCBBetterQuotes/SLCBBetterQuotes-git.zip -d ./tmp/SLCBBetterQuotes/; \
	cd ./tmp; \
	zip -r ../SLCBBetterQuotes.zip ./SLCBBetterQuotes/ -x ./SLCBBetterQuotes/SLCBBetterQuotes-git.zip; \
	cd ..; \
	rm -rf ./tmp;

clean:
	rm SLCBBetterQuotes.zip; \
	rm -rf ./venv;
