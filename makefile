init:
	python3 -m venv venv
	sh venv/bin/activate
	pip3 install -r requirements.txt

clean:
	rm -rf venv

activate:
	sh venv/bin/activate