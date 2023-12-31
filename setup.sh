sudo pip3 install -r requirements.txt

export DJANGO_SETTINGS_MODULE=voximplant_medsenger_bot.settings.production

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic

sudo cp voximplant_medsenger_bot.conf /etc/supervisor/conf.d/
sudo cp voximplant_nginx.conf /etc/nginx/sites-enabled/
sudo supervisorctl update
sudo systemctl restart nginx
sudo certbot --nginx -d voximplant.ai.medsenger.ru
#vim .env