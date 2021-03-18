
format:
	brunette . --config=setup.cfg
	isort .

lint:
	env PYTHONPATH=src pytest src --pylint --flake8 --mypy

lint-all:
	env PYTHONPATH=src pytest src --pylint --flake8 --mypy --cache-clear

utest:
	env PYTHONPATH=src pytest test/unittest/ -s --verbose --cov=src --cov-report=html --cov-report=term-missing

setup:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	pre-commit install

tree:
	tree -I "*data|.pkl|*.png|*.txt|$(shell cat .gitignore | tr -s '\n' '|' )"
