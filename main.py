from flask import Flask
app = Flask(__name__)

def sayHello():
    print("Hello")
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/greet/<username>')
def greet(username):
    return 'Hello '+username
@app.route('/farewell/<username>')
def bye(username):
    return 'Good Bye '+username

if __name__ == '__main__':
    app.run()