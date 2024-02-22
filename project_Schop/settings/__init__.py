import logging


from .settings_comon import *
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
load_dotenv()

if os.getenv('SETTINGS') == 'local':
    from .settings_local import *
    print('===== >>>>>>  settings_local  <<<<<<<< ========')
else:
    from .settings_prod import *
    print('===== >>>>>>  settings_prod  <<<<<<<< ========')
