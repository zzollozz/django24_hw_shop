import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#
# MEDIA_ROOT = BASE_DIR / 'media'

STATIC_ROOT = BASE_DIR / 'static/'
MEDIA_ROOT = BASE_DIR / 'media/'

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

DATABASES = {
    'default': {
        'NAME': os.getenv('DATABASES_NAME'),
        'ENGINE': os.getenv('DATABASES_ENGINE'),  # <your_username>$<your_database_name>
        'USER': os.getenv('DATABASES_USER'),      # <your_username
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': 'domshop.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET NAMES 'utf8mb4';SET sql_mode = 'STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        }
    }
}
