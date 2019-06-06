# FLASK_APP=test_webapp.py flask run
from flask import Flask as any_name, render_template
import urllib.request


#app = Flask(__name__)
app = any_name(__name__)

@app.route("/")
def flask():
    content = urllib.request.urlopen("http://127.0.0.1:8080").read()
    return render_template("index.html", time=content)
    #return content

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)