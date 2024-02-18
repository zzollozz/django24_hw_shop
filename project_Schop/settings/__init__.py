import os
from .settings_comon import *
from dotenv import load_dotenv


load_dotenv()

if os.getenv('SETTINGS') == 'local':
    from .settings_local import *
    print('settings_local')
else:
    from .settings_prod import *
    print('settings_prod')
