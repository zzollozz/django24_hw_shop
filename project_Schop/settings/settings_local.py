import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, '../static'),
# )
# MEDIA_ROOT = os.path.join(BASE_DIR, '../media')


# MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.parent / 'media/'

DATABASES = {
    'default': {
        'NAME': os.getenv('DATABASES_NAME'),
        'ENGINE': os.getenv('DATABASES_ENGINE'),
        'USER': os.getenv('DATABASES_USER'),
    }
}

