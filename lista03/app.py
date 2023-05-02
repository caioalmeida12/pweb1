from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def index(username):
    return (username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return ("post: " + str(post_id))

@app.route('/float/<float:float_id>')
def show_float(float_id):
    return ("float: " + str(float_id))

@app.route('/path/<path:path_id>')
def show_path(path_id):
    return ("path: " + path_id)

if __name__ == '__main__':
    app.run(debug=True)