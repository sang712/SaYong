# Deploying Django on AWS Lightsail

[toc]

## ๐จ ์ฃผ์์ฌํญ ๐จ

- ํญ์ ํฐ๋ฏธ๋์์์ ๋์ ์์น๋ฅผ ํ์ธํฉ๋๋ค.

- ๊ฐ์ํ๊ฒฝ์ด ํ์ฑํ๋์ด์๋์ง ํ์ธํฉ๋๋ค.

  

## ๊ฐ๋ฐํ๊ฒฝ

- Python 3.8.x
- Django 3.1.x



## Lightsail ์ ์ ๋ฐ ์ธ์คํด์ค ์์ฑ ํด๋ฆญ

![images/Untitled.png](images/Untitled.png)



## ์ธ์คํด์ค ์ด๋ฏธ์ง ๋ฐ OS ์ ํ

![images/Untitled%201.png](images/Untitled%201.png)



## ์ธ์คํด์ค ํ๋ ๋ฐ ์ธ์คํด์ค ์ด๋ฆ ์ง์ 

![images/Untitled%202.png](images/Untitled%202.png)



## ์ต์ข ์ธ์คํด์ค ์์ฑ

![images/Untitled%203.png](images/Untitled%203.png)



## ์ธ์คํด์ค ์์ฑ ํ์ธ

์ ์ ๊ธฐ๋ค๋ฆฌ๋ฉด Pending โ Running์ผ๋ก ๋ณ๊ฒฝ.

![images/Untitled%204.png](images/Untitled%204.png)



## ์ธ์คํด์ค ์ ์

![images/Untitled%205.png](images/Untitled%205.png)

![images/Screen_Shot_2019-10-07_at_9.50.02_AM.png](images/Screen_Shot_2019-10-07_at_9.50.02_AM.png)



## ๋ฐฐํฌ ์  Django ์ค์ 

> ๐จ **์ ์ ๋ก์ปฌ๋ก ๋์์์ Django๋ฅผ ์ค๋น์ํต๋๋ค.**

### requirements.txt

```bash
**(venv) # ๋ฐ๋์ ๊ฐ์ํ๊ฒฝ์ด ์ ์ฉ๋์๋์ง ํ์ธ!!**
pip freeze > requirements.txt
```



### settings.py ๋ถ๋ฆฌํ๊ธฐ

1. `settings` ํด๋๋ฅผ ์์ฑํฉ๋๋ค.
2. ๊ทธ ์์ `__init__.py` ํ์ผ์ ์์ฑํฉ๋๋ค.
3. ๊ธฐ์กด์ `settings.py` ํ์ผ์ `base.py`๋ก ๋ณ๊ฒฝํฉ๋๋ค.
4. `local.py` ๊ทธ๋ฆฌ๊ณ  `production.py` ํ์ผ์ ๋ ๊ฐ ์์ฑํฉ๋๋ค.

```python
settings/
  __init__.py
  base.py
  local.py
  production.py
```

### base.py

```python
# ๊ธฐ์กด settings.py์ ์๋ ๋ชจ๋  ๋ด์ฉ
```

### local.py

```python
# settings/local.py

from .base import *

DEBUG = True

ALLOWED_HOSTS = []
```

### production.py

- ๋ฐ๋์ ALLOWED_HOSTS์ Lightsail์ ํผ๋ธ๋ฆญ IP๋ฅผ ์์ฑํฉ๋๋ค.

```python
from .base import *

DEBUG = False

ALLOWED_HOSTS = [
 # lightsail public_ip ์ฃผ์
 # ex) 13.126.105.123
]
```

- aws console ์์ ๋ฐฐํฌํ ์๋ฒ ์ด๋ฆ ํด๋ฆญ

    ![images/Screen_Shot_2019-10-07_at_4.08.09_PM.png](images/Screen_Shot_2019-10-07_at_4.08.09_PM.png)

- ํผ๋ธ๋ฆญ IP ์ฃผ์ ํ์ธ

    ![images/Screen_Shot_2019-10-07_at_4.00.09_PM.png](images/Screen_Shot_2019-10-07_at_4.00.09_PM.png)

### wsgi.py

- **ํ๋ก์ ํธํด๋๋ช?**
    - `settings` ํด๋ ๋ฐ `wsgi.py`๊ฐ ์๋ ํด๋๋ฅผ ๋ปํฉ๋๋ค.

```bash
import os

...

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ํ๋ก์ ํธํด๋๋ช.settings.production')

...
```



### manage.py

- **ํ๋ก์ ํธํด๋๋ช?**
    - `settings` ํด๋ ๋ฐ `wsgi.py`๊ฐ ์๋ ํด๋๋ฅผ ๋ปํฉ๋๋ค.

```bash
#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ํ๋ก์ ํธํด๋๋ช.settings.local')
    ...
```



### static ๊ด๋ จ ์ค์ 

```python
# settings/base.py

STATIC_URL = '/static/'

STATICFILES_DIRS = [ 
	# ์ง์  ๋ง๋  static ํด๋์ ๊ฒฝ๋ก๋ฅผ ์ ์ต๋๋ค.
	# ex1) BASE_DIR / '์ฐ๋ฆฌํ_static_ํด๋๋ช'
  # ex2) BASE_DIR / config / 'static'
]

STATIC_ROOT = BASE_DIR / 'staticfiles'
```

```bash
python manage.py collectstatic
```



## ํ์ด์ฌ & ํ์ ํจํค์ง ์ค์น

> ๐จ **๋ก์ปฌ์์ ๋ค์ AWS Lightsail ํฐ๋ฏธ๋๋ก ๋์์ต๋๋ค.**

```bash
sudo apt-get update
sudo apt install gunicorn
sudo apt-get install gcc libpq-dev -y
sudo apt-get install python3-dev python3-pip libpq-dev python3-venv python3-wheel -y
sudo apt-get install nginx
pip3 install wheel
```

```bash
apt list --installed
```



## ํ๋ก์ ํธ Clone

```bash
git clone ํ๋ก์ ํธ์ฃผ์

cd ํ๋ก์ ํธ๋ช
```



## ํ์ด์ฌ ๊ฐ์ํ๊ฒฝ ์ค์ 

```bash
python3 -m venv venv
source venv/bin/activate
```



## ํ์ ํจํค์ง ์ค์น

```bash
pip3 install -r requirements.txt
pip3 install wheel
pip3 install gunicorn psycopg2
pip3 freeze > requirements.txt
```



## Gunicorn ์ค์ 

- **๋ฃจํธํด๋๋ช?** (final-pjt)
    - `manage.py`๋ฅผ ํฌํจํ๊ณ  ์๋ ํด๋๋ฅผ ๋ปํฉ๋๋ค.
- **ํ๋ก์ ํธํด๋๋ช?** (config)
    - `settings` ํด๋ ๋ฐ `wsgi.py`๊ฐ ์๋ ํด๋๋ฅผ ๋ปํฉ๋๋ค.

```bash
sudo vi /etc/systemd/system/gunicorn.service
```

```bash
# /etc/systemd/system/gunicorn.service

[Unit]
Description=ssafy5 gj final-pjt
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/๋ฃจํธํด๋๋ช
ExecStart=/home/ubuntu/๋ฃจํธํด๋๋ช/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/ubuntu/๋ฃจํธํด๋๋ช/๋ฃจํธํด๋๋ช.sock ํ๋ก์ ํธํด๋๋ช.wsgi:application

[Install]
WantedBy=multi-user.target
```

```bash
# /etc/systemd/system/gunicorn.service
# ์ด๊ณณ์์ ๋จผ์  ์์ฑํ ๋ค ํฐ๋ฏธ๋๋ก ๊ฐ๊ณ ๊ฐ์ ๋ถ์ฌ๋ฃ์ผ์ธ์!


```



## Gunicorn ์คํ

- `sudo systemctl status gunicorn` ๋ช๋ น์ด๋ฅผ ํตํด ์ค๋ฅ๊ฐ ์๋์ง ํ์ธํฉ๋๋ค.
- ์๋ ๋ช๋ น์ด ์๋ ฅ ํ `ํ๋ก์ ํธ๋ช.sock` ํ์ผ์ ์กด์ฌ ์ ๋ฌด๋ฅผ ํ์ธํฉ๋๋ค.

```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn
```



- ์๋ฌ๋ฐ์ ์ `/etc/systemd/system/gunicorn.service` ํ์ผ ์์ 
- ์์  ํ ์๋ ๋ช๋ น์ด๋ก ์ฌ์๋

```bash
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
```



## Nginx ์ค์ ํ๊ธฐ

- **๋๋ฉ์ธ๋ช ๋๋ lightsail_public_ip?**
    - lightsail์์ ์ ๊ณตํ๋ ํผ๋ธ๋ฆญ IP๋ฅผ ์ ์ด์ฃผ์๋ฉด ๋ฉ๋๋ค.
- **๋ฃจํธํด๋๋ช?**
    - `manage.py`๋ฅผ ํฌํจํ๊ณ  ์๋ ํด๋๋ฅผ ๋ปํฉ๋๋ค.

```bash
sudo vi /etc/nginx/sites-available/๋ฃจํธํด๋๋ช

ex) sudo vi /etc/nginx/sites-available/final-pjt
```

```bash
# sudo vi /etc/nginx/sites-available/๋ฃจํธํด๋๋ช

server {
    listen 80;
    server_name ๋๋ฉ์ธ๋ช_๋๋_lightsail_public_ip;

		location /static/ {
			alias /home/ubuntu/๋ฃจํธํด๋๋ช/staticfiles/;
		}

		location / {
			include proxy_params;
			proxy_pass http://unix:/home/ubuntu/๋ฃจํธํด๋๋ช/๋ฃจํธํด๋๋ช.sock;
		}
}
```

```bash
# sudo vi /etc/nginx/sites-available/๋ฃจํธํด๋๋ช
# ์ด๊ณณ์์ ๋จผ์  ์์ฑํ ๋ค ํฐ๋ฏธ๋๋ก ๊ฐ๊ณ ๊ฐ์ ๋ถ์ฌ๋ฃ์ผ์ธ์!


```

```bash
sudo ln -s /etc/nginx/sites-available/๋ฃจํธํด๋๋ช /etc/nginx/sites-enabled
```

```bash
# sudo ln -s /etc/nginx/sites-available/๋ฃจํธํด๋๋ช /etc/nginx/sites-enabled
# ์ด๊ณณ์์ ๋จผ์  ์์ฑํ ๋ค ํฐ๋ฏธ๋๋ก ๊ฐ๊ณ ๊ฐ์ ๋ถ์ฌ๋ฃ์ผ์ธ์!

```



## Nginx ๋์ ํ์ธ ๋ฐ ์ฌ์คํ

```bash
sudo nginx -t
```

```bash
sudo systemctl restart nginx
```



## Nginx ์๋ฌ๋ฐ์ ์ ์์  ํ ์ ์ฒด ์ฌ์คํ

```bash
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl restart nginx
```

