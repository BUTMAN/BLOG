from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import abort

from models import Blog
from models import BlogComment

from user import current_user


main = Blueprint('blog', __name__)


@main.route('/')
def index():
    u = current_user()
    if u is None:
        return redirect(url_for('user.login_view'))
    blogs = Blog.query.order_by(Blog.id.desc()).all()
    for i in blogs:
        i.comment = i.comments()
        for j in i.comment:
            j.avatar = j.get_avatar()
        i.comments_num = len(i.comment)
    return render_template('blog_index.html', blogs=blogs)


@main.route('/admin')
def admin():
    u = current_user()
    if u is None:
        return redirect(url_for('user.login_view'))
    blogs = Blog.query.order_by(Blog.id.desc()).all()
    for i in blogs:
        i.comment = i.comments()
        for j in i.comment:
            j.avatar = j.get_avatar()
        i.comments_num = len(i.comment)
    return render_template('blog_admin.html', blogs=blogs)


@main.route('/blogs')
def blogs():
    u = current_user()
    if u is None:
        return redirect(url_for('user.login_view'))
    blogs = Blog.query.order_by(Blog.id.desc()).all()
    for i in blogs:
        i.comment = i.comments()
        for j in i.comment:
            j.avatar = j.get_avatar()
        i.comments_num = len(i.comment)
    return render_template('blog_add.html', blogs=blogs)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    u = current_user()
    b = Blog(form)
    b.name = u.username
    if b.valid():
        b.save()
    return redirect(url_for('.blogs'))


@main.route('/comment', methods=['POST'])
def comment():
    form = request.form
    u = current_user()
    c = BlogComment(form)
    c.name = u.username
    if c.valid():
        c.save()
    c.avatar = c.get_avatar()
    return redirect(url_for('.blogs'))


@main.route('/delete/<int:weibo_id>')
def delete(weibo_id):
    w = Blog.query.get(weibo_id)
    w.delete()
    return redirect(url_for('.index'))
