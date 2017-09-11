from binascii import hexlify
from rest import app, init_db

import os

app.API_KEY = hexlify(os.urandom(20)).decode()
print('api key is: {}'.format(app.API_KEY))

dir_name = os.path.dirname(os.path.abspath(__file__))
app.config['DB_PATH'] = os.path.join(dir_name, 'schema')
app.config['DB_SOURCE'] = os.path.join(app.config['DB_PATH'], 'schema.sql')
app.config['DB_INSTANCE'] = os.path.join(app.config['DB_PATH'], 'schema.db')

app.config['DEBUG'] = True

init_db()
app.run(host='0.0.0.0')
