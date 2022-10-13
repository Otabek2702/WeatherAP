from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required

from web.models import DailyWeather, db, City, User
from .schemas import daily_weathers_schema, daily_weather_schema, city_schema
from web.schemas import user_schema

apiv0 = Blueprint('apiv0', __name__, url_prefix='/apiv0/')


@apiv0.route('/daily_weather/', methods=['GET'])
@jwt_required()
def get_daily_weathers():
    all_daily_weather = DailyWeather.query.order_by().all()
    return jsonify(daily_weathers_schema.dump(all_daily_weather))


@jwt_required()
@apiv0.route("/daily_weather/<id>, methods=['GET']")
def get_daily_weather(id):
    user = DailyWeather.query.get(id)
    return daily_weather_schema.dump(user)


@jwt_required()
@apiv0.route('/daily_weather/', methods=['POST'])
def create_daily_weather():
    data = request.get_json()
    daily_weather = DailyWeather(**data)
    db.session.add(daily_weather)
    db.session.commit()
    return daily_weather_schema.dump(daily_weather)


@jwt_required()
@apiv0.route('/daily_weather/<id>', methods=['PUT'])
def update_daily_weather(id):
    data: dict = request.get_json()
    daily_weather = DailyWeather.query.get(id)
    for key, value in data.items():
        setattr(daily_weather, key, value)
    db.session.commit()
    return daily_weather_schema.dump(daily_weather)


@jwt_required()
@apiv0.route('/daily_weather/<id>', methods=['DELETE'])
def delete_daily_weather(id):
    daily_weather = DailyWeather.query.get(id)
    db.session.delete(daily_weather)
    db.session.commit()
    return {"result": "deleted"}


# City
@jwt_required()
@apiv0.route('/city', methods=['GET'])
def citys():
    get_citys = City.query.order_by(City.id).all()
    return jsonify(city_schema.dump(get_citys, many=True))


@jwt_required()
@apiv0.route('/city/<int:id>', methods=['GET'])
def city(id):
    get_city = City.query.get(id)
    return city_schema.dump(get_city)


@jwt_required()
@apiv0.route('/city', methods=['POST'])
def create_city():
    data = request.get_json()
    c_city = City(**data)
    db.session.add(c_city)
    db.session.commit()
    return city_schema.dump(c_city)


@jwt_required()
@apiv0.route('/city/<int:id>', methods=['PUT'])
def update_city(id):
    data: dict = request.get_json()
    u_citys = City.query.get(id)
    for key, value in data.items():
        setattr(u_citys, key, value)
    db.session.commit()
    return city_schema.dump(u_citys)


@jwt_required()
@apiv0.route('/city/<int:id>', methods=['DELETE'])
def delete_city(id):
    d_city = City.query.get(id)
    db.session.delete(d_city)
    db.session.commit()
    return {"result": "deleted"}


@jwt_required()
@apiv0.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(**data)
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return user_schema.dump(user)


@jwt_required()
@apiv0.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(username)
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username or password"}), 401
