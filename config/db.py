from dotenv import load_dotenv
from os import environ, path, getenv


basedir = path.abspath(path.dirname(__name__))
print(basedir)
load_dotenv(path.join(basedir, '.env'))


class MongodbConfig(object):
    MONGODB_USERNAME = environ.get('MONGODB_USERNAME')
    MONGODB_PASSWORD = environ.get('MONGODB_PASSWORD')
    MONGODB_HOST = environ.get('MONGODB_HOST')
    MONGODB_PORT = int(environ.get('MONGODB_PORT'))
    MONGODB_DB = environ.get('MONGODB_DB')

    def __repr__(self) -> str:
        return f'mongodb://{self.MONGODB_USERNAME}:{self.MONGODB_PASSWORD}@{self.MONGODB_HOST}:{self.MONGODB_PORT}/{self.MONGODB_DB}'
