pip3 install uwsgi
uwsgi --http 0.0.0.0:8080 --wsgi-file app.py --callable app