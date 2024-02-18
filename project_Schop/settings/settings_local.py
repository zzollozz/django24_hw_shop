import os
from pathlib import Path
import environ



env = environ.Env(
    DEBUG=(bool, False)
)

BASE_DIR = Path(__file__).resolve().parent.parent

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, '../static'),
# )
# MEDIA_ROOT = os.path.join(BASE_DIR, '../media')

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

DATABASES = {
    'default': {
        'NAME': env.str('DATABASES_NAME'),
        'ENGINE': env.str('DATABASES_ENGINE'),
        'USER': env.str('DATABASES_USER'),
    }
}
