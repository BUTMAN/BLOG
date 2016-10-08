from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import abort
from flask import session

from models import User


main = Blueprint('user', __name__)


def current_user():
    uid = session.get('user_id')
    if uid is not None:
        u = User.query.get(uid)
        return u


@main.route('/')
def login_view():
    u = current_user()
    if u is not None:
        return redirect('/blog')
    return render_template('user_login.html')


@main.route('/user/register', methods=['POST'])
def register():
    form = request.form
    u = User(form)
    avatar = u.av()
    u.avatar = avatar
    if u.valid():
        u.save()
    else:
        abort(410)
    return redirect(url_for('blog.index'))


@main.route('/user/login', methods=['POST'])
def login():
    form = request.form
    u = User(form)
    user = User.query.filter_by(username=u.username).first()
    if user is not None and user.validate_login(u):
        print('登录成功')
        session['user_id'] = user.id
    else:
        print('登录失败')
    return redirect(url_for('.login_view'))


@main.route('/user/update_password', methods=['POST'])
def update_password():
    u = current_user()
    password = request.form.get('password', '')
    print('password', password)
    if u.change_password(password):
        print('修改成功')
    else:
        print('用户密码修改失败')
    return redirect('/profile')


@main.route('/user/update_avatar', methods=['POST'])
def update_avatar():
    u = current_user()
    avatar = request.form.get('avatar', '')
    print('password', avatar)
    if u.change_avatar(avatar):
        print('修改成功')
    else:
        print('用户密码修改失败')
    return redirect('/profile')


@main.route('/profile', methods=['GET'])
def profile():
    u = current_user()
    if u is not None:
        print('profile', u.id, u.username, u.password)
        return render_template('profile.html', user=u)
    else:
        return redirect(url_for('.login_view'))

