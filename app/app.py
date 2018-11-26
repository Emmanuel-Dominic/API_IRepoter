from flask import Flask
from app.views.incidents import incident_bp
# from views.users import user_bp

app = Flask(__name__)

app.register_blueprint(user_bp)
app.register_blueprint(incident_bp)


if __name__ == '__main__':
    app.run(debug=True)
