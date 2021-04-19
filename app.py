from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    print('Hello world')
    print('asdfasdfasdf')
    return 'Test GitHub!'


if __name__ == '__main__':
    app.run()
