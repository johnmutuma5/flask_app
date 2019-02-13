import os

class Config():
    DEBUG = True
    TESTING = True
    APP_SECRET = os.getenv('APP_SECRET')
    ENV = os.getenv('ENVIRONMENT')

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_DEV')

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_TEST')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_PROD')

env = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'test': TestingConfig
}[os.getenv('ENVIRONMENT')]
