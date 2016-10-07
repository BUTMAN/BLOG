from flask import Flask
from flask import render_template

from weibo import main as weibo_routes
from user import main as user_routes
from blog import main as blog_routes
from api import main as api_routes


app = Flask(__name__)
app.secret_key = 'fsdfhloip.ljhklh'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


app.register_blueprint(weibo_routes)
app.register_blueprint(user_routes)
app.register_blueprint(blog_routes, url_prefix='/blog')
app.register_blueprint(api_routes,
                       url_prefix='/api')


@app.errorhandler(404)
def error404(e):
    return render_template('404.html')


@app.errorhandler(410)
def error404(e):
    return render_template('410.html')


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=80,
        threaded=True,
    )
    app.run(**config)
