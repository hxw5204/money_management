class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    SECRET_KEY = '895402142'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1:3306/moneymanagement'
    SQLALCHEMY_TRACK_MODIFICATIONS = False




class TestingConfig(Config):
    TESTING = True
