from flask import Flask, request, jsonify, make_response, redirect, url_for, flash
from flask_restful import Resource, Api
from db.db import User, Books, Author
app = Flask(__name__)
api = Api(app)

# Configure JWT
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

# Assuming you have CORS middleware installed
# from flask_cors import CORS
# CORS(app)

@app.route('/login/user', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form['userName']
        password = request.form['passwd']
        remember = True if request.form.get('remember') else False

        # Authenticate user locally
        user = User.query.filter_by(username=username).first()
        if user and user.validate_pass(password):
            access_token = create_access_token(identity=user.id)

            # Set JWT token as a cookie
            response = make_response(jsonify(message='success', access_token=access_token))
            response.set_cookie('access_token_cookie', access_token, secure=True, httponly=True)
            
            # Redirect based on user type
            if user.usertype == 'Listener':
                return redirect(url_for('hello'))
            else:
                flash("Invalid Credentials")
        else:
            flash("Invalid Credentials")

    return render_template('user/base.html')

class UserLogin(Resource):
    def post(self):
        username = request.form['userName']
        password = request.form['passwd']

        # Authenticate user using API
        response = requests.post('http://localhost:5000/api/login', data={
            'userName': username,
            'passwd': password
        })

        if response.status_code == 200:
            data = response.json()
            if data.get('usertype') == 'Listener':
                return redirect(url_for('routes.hello'))
            else:
                flash("Invalid Credentials")
        else:
            flash("Invalid Credentials")

api.add_resource(UserLogin, '/api/login')

if __name__ == '__main__':
    app.run(debug=True)
