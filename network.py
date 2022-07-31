import flask
from flask import request, jsonify,render_template, send_file, g
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/1', methods=['GET'])
def one():
    ip=request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    port=7000
    print(request.headers,flush=True)
    return render_template("1.html",ip=ip,port=port)
@app.after_request
def after_request_func(response):
    print(response.get_data(as_text=False))
@app.route('/2', methods=['GET'])
def two():
    print(request.headers,flush=True)
    return render_template("2.html")
@app.after_request
def after_request_func(response):
    print(response.get_data(as_text=False))
@app.route('/3', methods=['GET'])
def three():
    print(request.headers,flush=True)
    return send_file('python.png')
@app.after_request
def after_request_func(response):
    print(response.get_data(as_text=False))
if __name__ == '__main__':
    app.run(port=7000)