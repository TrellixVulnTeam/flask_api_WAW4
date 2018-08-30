def db_config(app):
    app.secret_key = 'flask API app secret key'
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
    app.config['MYSQL_DATABASE_DB'] = 'flask_test'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    return app