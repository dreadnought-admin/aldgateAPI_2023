set -o errexit
pip install --upgrade pip
pip install -r ./api/requirements.txt
poetry install
python manage.py collectstatic --no-input
python manage.py migrate
