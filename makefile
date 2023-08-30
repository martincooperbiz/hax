create-env:
	@pip3 install virtualenv && \
	python3 -m venv ./.venv && \
	source ./.venv/bin/activate &&\
	python3 -m pip install -r hax/requirements.txt

install-tk:
	@brew install python-tk

run:
	@python3 hax/main.py

install-website:
	@cd website/webapp && \
	npm install

build-website:
	@cd website/webapp && \
	npm run build

run-website:
	@cd website/webapp && \
	npx serve@latest out
