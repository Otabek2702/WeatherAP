import datetime

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.String(30), nullable=True, default='')
    last_name = db.Column(db.String(30), nullable=True, default='')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r>' % self.username


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weatherURL = db.Column(db.Text)
    cityName = db.Column(db.String(30))
    state = db.Column(db.String(30))

    def __repr__(self):
        return '<City %r>' % self.cityName


class YearlyWeather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)

    def __repr__(self):
        return '<YearlyWeather %r>' % self.city_id


class MonthlyWeather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)

    def __repr__(self):
        return '<MonthlyWeather %r>' % self.city_id


class HourlyWeather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)

    def __repr__(self):
        return '<WeaklyWeather %r>' % self.city_id


class DailyWeather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    high_temp = db.Column(db.Integer, nullable=False)
    low_temp = db.Column(db.Integer, nullable=False)
    avg_temp = db.Column(db.Integer, nullable=False)
    wind = db.Column(db.Integer, nullable=False)
    compass = db.Column(db.String(20), nullable=False)
    weather_type = db.Column(db.String(30), nullable=False)
    humidity = db.Column(db.Integer, nullable=False)

    @property
    def city_name(self):
        city_name = City.query.get(self.city_id)
        return city_name.cityName

    def __repr__(self):
        return '<DailyWeather %r>' % self.date
