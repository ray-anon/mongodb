
from app.routes.user import user

def register_routes(app):
    app.register_blueprint(user, url_prefix='/user')
