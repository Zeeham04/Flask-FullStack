from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'NAZEEH'

    from .views import views
    from .auth import auth

    # Keep views at '/'
    app.register_blueprint(views, url_prefix='/')

    # Remove url_prefix for auth to make routes directly accessible
    app.register_blueprint(auth)

    return app

