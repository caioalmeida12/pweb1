from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def index(username):
    return (username)

if __name__ == '__main__':
    app.run(debug=True)