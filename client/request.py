# FLASK_APP=test_webapp.py flask run
from flask import Flask as any_name, render_template
from urllib.request import urlopen



#app = Flask(__name__)
app = any_name(__name__)

@app.route("/")
def flask():
    content = urlopen("http://172.17.0.2:8080").read()
    return render_template("index.html", time=content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
