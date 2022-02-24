import os
from pathlib import Path

from dotenv import load_dotenv

basedir = Path(__file__).parent.resolve()
load_dotenv(basedir.joinpath('.env'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
        'postgres://',
        'postgresql://') or f'sqlite:///{basedir.joinpath("app.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['cespenar1@gmail.com']
    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'pl']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    MS_TRANSLATOR_LOCATION = os.environ.get('MS_TRANSLATOR_LOCATION')
    OPENSEARCH_URL = os.environ.get('OPENSEARCH_URL')
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
