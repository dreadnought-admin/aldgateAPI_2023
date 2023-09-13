set -o errexit
pip install --upgrade pip
pip install django
pip3 install django
pip install django_rest_framework
pip3 install django_rest_framework
pip install django-cors-headers
pip3 install django-cors-headers
pip install whitenoise
pip3 install whitenoise
pip3 install psycopg2 gunicorn
pip3 freeze > requirements.txt
pip install -r requirements.txt
pip3 install -r requirements.txt
python api/manage.py migrate
