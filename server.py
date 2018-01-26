from flask import Flask, url_for, Request, jsonify
from employee import Employee

app = Flask(__name__)


@app.route('/rs4654748')
def vitaminB():
    r = requests.get('https://api.23andme.com/3/marker/rs10195681/')
    return r.text

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

@app.route('/json_api')
def api_hello():
    return 'hello'
    # data = {
    #     'hello'  : 'world',
    #     'number' : 3
    # }
    # js = json.dumps(data)
    #
    # resp = jsonify(data)
    # resp.status_code = 200
    # resp.headers['Link'] = 'http://luisrei.com'
    #
    # return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
