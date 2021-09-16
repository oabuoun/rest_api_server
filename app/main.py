from flask import Flask, request

flask_app = Flask(__name__)

@flask_app.route('/')
def index_func():
    return "Welcome to this server, this is the root"

@flask_app.route('/test')
def test_func():
    return "This is the testing service"

@flask_app.route('/person/<int:person_id>')
def person_get(person_id):
    print(f"This is the /person route, person_id = {person_id}")
    return f"You asked for the details of {person_id}"

@flask_app.route('/info')
def info_get():
    print("This is the /info route")
    print(request.args)
    for key in request.args:
        print(f"{key} has a value of {request.args[key]}")
    return f"You visited the /info route, {request.args}"

@flask_app.route('/create_info', methods = ['POST'])
def create_inf_func():
    print("This is a POST request")
    print(request.form)
    for key in request.form:
        print(f"POST param: {key} = {request.form[key]}")
    return "You sent a POST request"

@flask_app.route('/create_server/<int:server_num>', methods = ['POST'])
def create_server(server_num):
    print("This is /create_server route")
    print(f"Server Num: {server_num}")
    for key in request.form:
        print(f"POST param: {key} = {request.form[key]}")
    return "The server was created successfully "

if __name__ == "__main__":
    print("Welcome to REST API Server")
    flask_app.run(host="0.0.0.0", port = 8080, debug=True)
