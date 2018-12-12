import os
# BASE_DIR = os.path.dirname(os.path.dirname(file))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '../static'),
]
STATIC_ROOT = BASE_DIR+'/static/'
STATIC_URL = '/static/' 