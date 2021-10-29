python -m autoflake --in-place --remove-all-unused-imports --ignore-init-module-imports -r julia_set_visualizer setup.py tests
python -m isort --profile black julia_set_visualizer setup.py tests
python -m black julia_set_visualizer setup.py tests
python -m mypy --strict --implicit-reexport julia_set_visualizer setup.py tests
python -m pylint julia_set_visualizer setup.py
python -m pytest tests
