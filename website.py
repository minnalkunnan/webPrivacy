#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, render_template

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'minnal'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

if __name__ == '__main__':
    app.run(debug=True)