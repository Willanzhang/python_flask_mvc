from flask import Flask, url_for, render_template
from imooc import route_imooc
from api import route_api
from common.libs.UrlManager import UrlManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint(route_imooc, url_prefix="/imooc")
app.register_blueprint(route_api, url_prefix="/api")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1/test'
db = SQLAlchemy(app)


@app.route('/')
def say_hello():
    url = url_for('safe')

    url_1 = UrlManager.buildUrl("/api")
    url_2 = UrlManager.buildUrl("/css/index.css")

    msg = 'hello world,url:%s, url_1:%s, url_2%s' % (url, url_1, url_2)
    from sqlalchemy import text
    sql = text("select * from users4")
    result = db.engine.execute(sql)

    for person in result:
        app.logger.info(person)
    # app.logger.error(msg)
    # app.logger.debug('A value for debugging')
    # app.logger.info('A value for info')
    # app.logger.warning('A warning occurred (%d apples)', 42)
    # app.logger.error('An error occurred')
    return msg


@app.route('/hehe')
def safe():
    return 'hehe page,'


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
