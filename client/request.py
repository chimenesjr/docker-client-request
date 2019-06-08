# FLASK_APP=test_webapp.py flask run
from flask import Flask as any_name, render_template
from urllib.request import urlopen

#app = Flask(__name__)
app = any_name(__name__)

@app.route("/")
def flask():
    content = urlopen("http://server:8080").read()
    return render_template("index.html", time=content)

@app.route("/test/")
def test():
    return 'working'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
