from flask import render_template, Blueprint, request, redirect
from .models import User, db, DailyWeather, City
import datetime

bp = Blueprint('weather', __name__, url_prefix='/')


@bp.route('/test', methods=['GET', 'POST'])
def view_test():
    html = ''
    if request.method == 'GET':
        for item in User.query.all():
            html += f"{item.username} {item.email} {item.password}<br>"
        html += '<a href="/test/create">Create</a>'
    return html


@bp.route('/test/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        data = request.form
        print(request.form)
        user = User(username=data['username'], email=data['email'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return redirect('/test')
    return render_template('test.html')


@bp.route('/')
def main():  # put application's code here

    req = request.args.get('city')
    time = datetime.date.today()
    data = DailyWeather.query.filter_by(date=time).first()
    print(data)

    return render_template('index.html',
                           today=data,
                           second=data,
                           third=data,
                           fourth=data,
                           fifth=data,
                           sixth=data,
                           seventh=data)


@bp.route('/news')
def news():
    return render_template('news.html')


@bp.route('/contact')
def contact():
    return render_template('contact.html')


@bp.route('/live-cameras')
def live_cameras():
    return render_template('live-cameras.html')


@bp.route('/photos')
def photos():
    return render_template('photos.html')


@bp.route('/single')
def single():
    return render_template('single.html')
