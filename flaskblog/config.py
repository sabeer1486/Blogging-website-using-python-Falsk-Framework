
class Config:
	SECRET_KEY = 'cf1e97eed22864b10508978a1af8e401'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
      username="PostCaro",
      password="7AM87VTghKhiAj5",
      hostname="PostCaro.mysql.pythonanywhere-services.com",
      databasename="PostCaro$postcaro",
    )
	SQLALCHEMY_POOL_RECYCLE = 299
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'shaiksabeer01@gmail.com'
	MAIL_PASSWORD = '@Sweety3333'

# class Config:
# 	SECRET_KEY = 'cf1e97eed22864b10508978a1af8e401'
# 	# SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
# 	SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
#        username="root",
#        password="sabeer",
#        hostname="127.0.0.1",
#        databasename="postcaro",
#     )
# 	SQLALCHEMY_POOL_RECYCLE = 299
# 	SQLALCHEMY_TRACK_MODIFICATIONS = False
# 	MAIL_SERVER = 'smtp.gmail.com'
# 	MAIL_PORT = 587
# 	MAIL_USE_TLS = True
# 	MAIL_USERNAME = 'shaiksabeer01@gmail.com'
# 	MAIL_PASSWORD = '@Sweety3333'