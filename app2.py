from flask import Flask, render_template
from jinja2 import FileSystemLoader, Environment

app = Flask(__name__)

@app.route('/index2')
def index2():
    message = "Hello!"
    return render_template('index2.html', message=message)

if __name__ == "__main__":
    app.run()