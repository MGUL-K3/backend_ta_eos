echo -e "\e[34mLint with isort\e[0m"
isort . --skip migrations --skip manage.py --skip venv

echo -e "\n\e[34mLint with black\e[0m"
black . --exclude "(migrations|manage.py|venv)" --line-length 79

echo -e "\n\e[34mLint with flake8\e[0m"
flake8 . --format github --exclude "migrations, manage.py, venv"

echo -e "\n\e[34mLint with mypy\e[0m"
mypy . --ignore-missing-imports --exclude "(migrations|manage.py|venv)"
echo -e ""
