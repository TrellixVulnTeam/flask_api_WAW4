from flask_restful import Resource, Api, reqparse


# Func : 사용자등록
class RegisterUser(Resource):
    def __init__(self, mysql):
        self.mysql = mysql

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

            data = register_db_conn(input_data, self.mysql)

            if len(data) > 0:
                return {'Message': data[0][0]}
            else:
                return {'Message': 'Fail'}
        except Exception as e:
            return {'Error': str(e)}


def register_db_conn(data, mysql):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_api_signup_insert', (data['_id'], data['_pwd'], data['_name'], data['_email']))
    result = cursor.fetchall()
    conn.commit()
    return result
