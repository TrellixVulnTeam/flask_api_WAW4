from flask import Flask
from flask_restful import Api
from flaskext.mysql import MySQL
import config
from api_get_user import GetUser
from api_register import RegisterUser

mysql = MySQL()
app = Flask(__name__)
api = Api(app)
mysql.init_app(config.db_config(app))

api.add_resource(GetUser, '/get_user', resource_class_kwargs={'mysql': mysql})
api.add_resource(RegisterUser, '/register_user', resource_class_kwargs={'mysql': mysql})

if __name__ == '__main__':
    app.run(debug=True)