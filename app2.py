from flask import Flask, render_template
from jinja2 import FileSystemLoader, Environment

app = Flask(__name__)

@app.route('/index2')
def index2():
    message = "Hello!"
    return render_template('index2.html', message=message)

@app.route('/dict_page')
def dict_page():
    tmp_dict = {}
    tmp_dict["name"]="Roj"
    tmp_dict["city"]="Manila"
    return render_template('dict_page.html',records=tmp_dict)

if __name__ == "__main__":
    app.run()