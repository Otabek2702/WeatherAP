from flask import Flask
from flask_jwt_extended import JWTManager

from web.views import bp as weather_bp
from web.admin import admin as admin_bp
from web.models import db
from web.schemas import ma as ma_user
from apiv0.views import apiv0 as apiv0_bp
from apiv0.schemas import ma as ma_model


app0 = Flask(__name__, template_folder='templates', static_url_path='/static')
app0.template_folder = 'templates'
app0.config.from_mapping(SECRET_KEY='dev')
app0.config['JWT_SECRET_KEY'] = "super-secret"  # Change this!
jwt = JWTManager(app0)

app0.register_blueprint(weather_bp)
app0.register_blueprint(admin_bp)
app0.register_blueprint(apiv0_bp)

app0.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flaskadmin:admin@localhost/flask_db'
app0.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app0
db.init_app(app0)

ma_model.init_app(app0)
ma_user.init_app(app0)

if __name__ == '__main__':
    app0.run()
