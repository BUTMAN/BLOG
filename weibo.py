from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import abort

from models import Weibo
from models import Comment

from user import current_user


main = Blueprint('weibo', __name__)


@main.route('/weibo')
def index():
    u = current_user()
    if u is None:
        return redirect(url_for('user.login_view'))
    weibo_list = Weibo.query.order_by(Weibo.id.desc()).all()
    for i in weibo_list:
        i.comment = i.comments()
        for j in i.comment:
            j.avatar = j.get_avatar()
        i.comments_num = len(i.comment)
        i.avatar = i.get_avatar()
    return render_template('weibo_index.html', weibos=weibo_list)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    u = current_user()
    t = Weibo(form)
    t.name = u.username
    if t.valid():
        t.save()
    return redirect(url_for('.index'))


@main.route('/comment', methods=['POST'])
def comment():
    form = request.form
    u = current_user()
    c = Comment(form)
    c.name = u.username
    if c.valid():
        c.save()
    return redirect(url_for('.index'))


@main.route('/delete/<int:weibo_id>')
def delete(weibo_id):
    w = Weibo.query.get(weibo_id)
    w.delete()
    return redirect(url_for('.index'))
