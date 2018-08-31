from flask_restful import Resource, Api, reqparse


# Func : 사용자 검색
class GetUser(Resource):
    def __init__(self, mysql):
        self.mysql = mysql

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('loginID', type=str)
            args = parser.parse_args()

            input_data = {
                '_id': args['loginID']
            }

            data = getuser_db_conn(input_data, self.mysql)

            if len(data) > 0:
                result = []
                for i in data:
                    tmp = {'LoginID': i[0], 'Name': i[1], 'Email': i[2]}
                    result.append(tmp)
                return result
            else:
                return {'Message': 'No ID matches!'}
        except Exception as e:
            return {'Error': str(e)}


def getuser_db_conn(data, mysql):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_api_getuser_select', [data['_id']])
    result = cursor.fetchall()
    conn.commit()
    return result



