# learning_python

A personal Python learning repository focused on fundamentals, code quality, and engineering discipline.

## Purpose

This repository is used to study Python fundamentals for applied development and quantitative engineering:

- core syntax and control flow
- functions, type hints, and docstrings
- basic data modeling with `dataclasses`
- code quality with Ruff
- static type checking with Pyright
- disciplined repository structure for saved exercises

## Repository structure

- `exercises/` — saved standalone Python exercises
- `.vscode/settings.json` — project-level VS Code settings
- `.gitignore` — ignored virtual environment, caches, local scratch files, and system files
- `README.md` — repository overview and usage notes

## Environment

This project uses:

- Python 3.11.8 managed with `pyenv`
- local virtual environment in `.venv`
- Ruff for formatting and linting
- Pyright for static type checking

Activate the environment before working in the terminal:

~~~bash
source .venv/bin/activate
~~~

## Run

Example:

~~~bash
python exercises/01_single_trade_pnl.py
python exercises/02_net_pnl_calculator.py
python exercises/03_order_book.py
~~~

## Quality checks

Run quality checks before considering an exercise finished:

~~~bash
ruff format exercises/
ruff check exercises/
pyright exercises
~~~

## Notes

- `practice.py` is kept local as a scratchpad and is not tracked in GitHub.
- Saved exercises are committed only after they run cleanly and pass formatting, linting, and type checks.
- Code that does not pass `python`, `ruff`, and `pyright` is considered unfinished.