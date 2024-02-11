from dotenv import load_dotenv
import os

load_dotenv()

# Application
APP_HOST = os.environ.get('APP_HOST')
APP_PORT = int(os.environ.get('APP_PORT'))

# Postgres
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
