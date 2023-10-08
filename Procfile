release: python manage.py makemigrations && python manage.py migrate
web: gunicorn aminata_project.wsgi --log-file -
