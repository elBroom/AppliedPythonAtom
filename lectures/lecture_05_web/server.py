import uuid

from flask import Flask, abort, request, jsonify

# export FLASK_ENV=development
# export FLASK_APP=server.py
# flask run
app = Flask(__name__)
filename = '/tmp/technoatom_lecture_05_web.tsv'
memory = {}
try:
    with open(filename) as f:
        for line in f:
            key, name, surname = line.split('\t')
            memory[key] = (name, surname)
except IOError:
    pass


#token = requests.post(
#     'http://127.0.0.1:5000/auth', 
#     json={'name': 'Zarina', 'surname': 'Sayfullina'}
# ).json()['token']
@app.route('/auth', methods=['POST'])
def auth():
    content = request.json
    if not content:
        return abort(418)

    name, surname = content.get('name'), content.get('surname')
    if not name or not surname:
        return abort(400)

    app.logger.debug('Welcome %s %s!', name, surname)

    token = str(uuid.uuid4())
    memory[token] = (name, surname)
    with open(filename, 'a+') as f:
        f.write('\t'.join([token, name, surname]) + '\n')
    return jsonify({'token': token})

# requests.get(
#     'http://127.0.0.1:5000/user_info', 
#     headers={'Authorization': 'Bearer ' + token}
# ).json()
@app.route('/user_info', methods=['GET'])
def user_info():
    token = request.headers.get('Authorization')
    if not token:
        return abort(400)

    token = token.replace('Bearer ', '')
    if token not in memory:
        return abort(401)

    name, surname = memory[token]
    app.logger.debug('Hello %s %s!', name, surname)
    return jsonify({'name': name, 'surname': surname})

