from flask import Flask, jsonify
from views.incidents import incident_bp
# from views.users import user_bp

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    """docstring function that return all redflags detials"""
    return jsonify({
                "status": 200,
                "data": 'Hello'
            }), 200




# app.register_blueprint(user_bp)
app.register_blueprint(incident_bp)


if __name__ == '__main__':
    app.run(debug=True)
