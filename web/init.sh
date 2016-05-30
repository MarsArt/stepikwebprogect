
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

#sudo gunicorn -c /home/box/web/etc/hello.py hello:application --daemon
#sudo gunicorn -c /home/box/web/etc/django.py ask.wsgi:application --error-logfile /home/box/web/gunic.log --daemon