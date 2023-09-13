set -o errexit
pip install --upgrade pip
pip3 freeze > requirements.txt
pip3 install -r requirements.txt
poetry install
python manage.py collectstatic --no-input
python manage.py migrate
