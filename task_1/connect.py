from mongoengine import connect
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'USER')
mongodb_pass = config.get('DB', 'PASS')
db_name = config.get('DB', 'DB_NAME')
domain = config.get('DB', 'DOMAIN')
options = config.get('DB', 'OPTIONS')

connect(host=f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?{options}", ssl=True)

