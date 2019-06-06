# FLASK_APP=test_webapp.py flask run
from flask import Flask as any_name

#app = Flask(__name__)
app = any_name(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/static")
def static_content():
    return app.send_static_file("static.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
