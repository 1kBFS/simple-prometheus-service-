nohup uwsgi --http 0.0.0.0:8080 --wsgi-file app.py --callable app > uwsgi.log 2>&1 &
echo "Deployed"