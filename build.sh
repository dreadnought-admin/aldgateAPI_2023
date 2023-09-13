set -o errexit
pip install --upgrade pip
pip3 freeze > requirements.txt
pip3 install -r requirements.txt
python api/manage.py collectstatic --no-input
python api/manage.py migrate
