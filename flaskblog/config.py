
class Config:
	SECRET_KEY = 'cf1e97eed22864b10508978a1af8e401'
	
	# if you are using file system as database
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	
	# if you are using sql server database
	SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
      	username="server_username",	# user sqlserver configuration here
      	password="serve_password",	# user sqlserver configuration here
      	hostname="server_host_name",	# user sqlserver configuration here
      	databasename="database_name",	# user sqlserver configuration here
    )
	SQLALCHEMY_POOL_RECYCLE = 299
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = '************@gmail.com' # enter your email for password reset request
	MAIL_PASSWORD = '*******' # your gamil password for sending password reset mail from your mail
