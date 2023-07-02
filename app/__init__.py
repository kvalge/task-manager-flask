from flask import Flask

from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.tasks.bills import bp as bills_bp
    app.register_blueprint(bills_bp, url_prefix='/bills')

    from app.tasks.entertainment import bp as entertainment_bp
    app.register_blueprint(entertainment_bp, url_prefix='/entertainment')

    from app.tasks.job import bp as job_bp
    app.register_blueprint(job_bp, url_prefix='/job')

    from app.tasks.studies import bp as studies_bp
    app.register_blueprint(studies_bp, url_prefix='/studies')

    from app.tasks.weather import bp as weather_bp
    app.register_blueprint(weather_bp, url_prefix='/weather')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
