import os
from pathlib import Path
import environ



env = environ.Env(
    DEBUG=(bool, False)
)
BASE_DIR = Path(__file__).resolve().parent.parent

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#
# MEDIA_ROOT = BASE_DIR / 'media'

STATIC_ROOT = BASE_DIR / 'static/'
MEDIA_ROOT = BASE_DIR / 'media/'


DATABASES = {
    'default': {
        'NAME': env.str('DATABASES_NAME'),
        'ENGINE': env.str('DATABASES_ENGINE'),  # <your_username>$<your_database_name>
        'USER': env.str('DATABASES_USER'),      # <your_username
        'PASSWORD': env.str('MYSQL_PASSWORD'),
        'HOST': 'domshop.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET NAMES 'utf8mb4';SET sql_mode = 'STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        }
    }
}
