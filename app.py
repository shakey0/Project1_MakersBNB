import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/
@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/signup', methods=['GET'])
def get_signup():
    return render_template('signup.html')

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def post_login():
    return redirect('/available-spaces')

@app.route('/available-spaces', methods=['GET'])
def get_available_spaces():
    return render_template('available_spaces.html')

'''
GET /new-space
Returns heading
'Enter new space details'
'''
@app.route('/new-space', methods=['GET'])
def add_new_space():
    return render_template('new_space.html')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
