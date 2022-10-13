from flask_marshmallow import Marshmallow
from web.models import City

ma = Marshmallow()


class DailyWeatherSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'date', 'city_id', 'high_temp', 'low_temp', 'avg_temp', 'wind', 'compass', 'weather_type', 'humidity')


daily_weather_schema = DailyWeatherSchema()
daily_weathers_schema = DailyWeatherSchema(many=True)


class CitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = City
        fields = ['id', 'weatherURL', 'cityName', 'state']


city_schema = CitySchema()
