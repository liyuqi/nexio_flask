from flask import Flask, url_for
from flask import json
from flask import request

app = Flask(__name__)
users = [{
    "id":1,
    "name": "Charles",
    "job_title": "SRE",
    "communicate_information": {
        "email": "charles@gmail.com",
        "mobile": "09xx-xxx-xxx"
    }
}]

@app.errorhandler(400)
def bad_request(error):
    return json.dumps({'status':400,'error': 'Bad request'})

@app.errorhandler(404)
def not_found(error):
    return json.dumps({'status': 404, 'error': 'Not found'})

@app.route('/')
def home():
    return json.dumps({"status": 200})

def make_user(user):
    new_user = {}
    for field in user:
            new_user[field] = user[field]
    return new_user

@app.route("/api/user", methods=['GET'])
def get_users():
    return json.dumps({"status": 200, 'users': list(map(make_user, users))})

@app.route("/api/user/<int:user_id>", methods=['GET'])
def get_user(user_id):
    user = list(filter(lambda t: t['id'] == user_id, users))
    if len(user) == 0:
        return json.dumps({"status": 404, 'user': "id not found"})
    return json.dumps({"status": 200, 'user':make_user(user[0])})

@app.route("/api/user", methods=['POST'])
def add_user():
    if not request.json or not 'name' in request.json:
        return json.dumps({'status': 400, 'error': 'Bad request'})
    user = {
        'id': users[-1]['id'] + 1,
        'name': request.json['name'],
        'job_title': request.json.get('job_title', ""),
    }
    users.append(user)
    return json.dumps({"status": 200, '+user': user})

@app.route("/api/user/<int:user_id>", methods=['PUT'])
def mod_user(user_id):
        user = list(filter(lambda t: t['id'] == user_id, users))
        if len(user) == 0:
            return json.dumps({"status": 404, 'user': "id not found"})
        if not request.json:
            return json.dumps({"status":404,'user':'not found'})
        if 'name' in request.json:
            user[0]['name'] = request.json.get('name', user[0]['name'])
        if 'job_title' in request.json:
            user[0]['job_title'] = request.json.get('job_title', user[0]['job_title'])
        return json.dumps({"status": 200, '^user':make_user(user[0])})

@app.route("/api/user/<int:user_id>", methods=['DELETE'])
def del_user(user_id):
    user = list(filter(lambda t: t['id'] == user_id, users))
    if len(user) == 0:
        return json.dumps({"status": 404, 'user': "id not found"})
    users.remove(user[0])
    return json.dumps({"status": 200, '-user':user})

if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )
