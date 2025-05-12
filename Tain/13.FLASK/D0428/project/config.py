import os
BASE_DIR=os.path.dirname(__file__)
DB_NAME='myweb.db'
SQLALCHEMY_DATABASE_URI='sqlite:///{}'.format(os.path.join(BASE_DIR,DB_NAME))
SQLALCHEMY_TRACK_MODIFICATIONs=False