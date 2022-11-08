import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
load_dotenv()

url = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')
print('sqlite:/' + os.path.join(basedir, 'app.db'))
