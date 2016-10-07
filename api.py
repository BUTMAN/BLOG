from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import abort

import json

from models import Weibo
from models import Comment

from user import current_user


main = Blueprint('api', __name__)


@main.route('/weibo/add', methods=['POST'])
def add():
    print('4455')
    form = request.form
    u = current_user()
    t = Weibo(form)
    t.name = u.username
    r = {
        'data': []
    }
    if t.valid():
        t.save()
        r['success'] = True
        r['data'] = t.json()
    else:
        r['success'] = False
        message = t.error_message()
        r['message'] = message
    print('123321')
    return json.dumps(r, ensure_ascii=False)


@main.route('/weibo/delete/<int:weibo_id>', methods=['GET'])
def delete(weibo_id):
    u = current_user()
    w = Weibo.query.get(weibo_id)
    if w.name == u.username:
        w.delete()
        r = {
            'success': True,
            'data': w.json(),
        }
    else:
        r = {
            'success': False,
            'data': w.json(),
        }
    return json.dumps(r, ensure_ascii=False)


@main.route('/weibo/update/<int:weibo_id>', methods=['POST'])
def update(weibo_id):
    print('1234')
    form = request.form
    w = Weibo.query.get(weibo_id)
    u = current_user()
    t = Weibo(form)
    print('debug', w.weibo, '1', t.weibo, '2', t.name, '3', u.username, '4', w.name, '5')
    r = {
        'data': []
    }
    if w.name == u.username:
        print('233')
        if t.valid():
            w.weibo = t.weibo
            w.save()
            r['success'] = True
            r['data'] = t.json()
            print('3344')
        else:
            r['success'] = False
            message = t.error_message()
            r['message'] = message
            print('4455')
    else:
        print('332')
        r['success'] = False
        r['message'] = '暗搓搓的改别人微博你这价值观有问题啊'
    return json.dumps(r, ensure_ascii=False)
