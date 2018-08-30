from flask import Flask
from flask_restful import Resource, Api, reqparse
from flaskext.mysql import MySQL
import config

mysql = MySQL()
app = Flask(__name__)
api = Api(app)
mysql.init_app(config.db_config(app))


# Func : 사용자등록
class RegisterUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('loginID', type=str)
            parser.add_argument('password', type=str)
            parser.add_argument('user_name', type=str)
            parser.add_argument('email', type=str)
            args = parser.parse_args()

            input_data = {
                '_id': args['loginID'],
                '_email':  args['email'],
                '_name': args['user_name'],
                '_pwd': args['password']
            }

            data = api_db_conn(input_data)

            if len(data) > 0:
                return {'Message': data[0][0]}
            else:
                return {'Message': 'Fail'}
        except Exception as e:
            return {'Error': str(e)}


api.add_resource(RegisterUser, '/register_user')


def api_db_conn(data):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_api_signup_insert', (data['_id'], data['_pwd'], data['_name'], data['_email']))
    result = cursor.fetchall()
    conn.commit()
    return result

#
# class GetUser(Resource):
#     def post(self):
#         try:
#             parser = reqparse.RequestParser()
#             parser.add_argument('loginID', type=str)
#             args = parser.parse_args()
#
#             input_data = {
#                 '_id': args['loginID'],
#             }
#
#             data = api_db_conn(input_data)
#
#             if len(data) > 0:
#
# 
#         except Exception as e:
#             return {'Error': str(e)}



if __name__ == '__main__':
    app.run(debug=True)