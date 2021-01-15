from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__)

tpl_text = 'My name is {{ name }}. I love {{ lang }} so much'
template = Template(tpl_text)

data = {'name': 'Taro', 'lang': 'Python'}
disp_text = template.render(data)
print(disp_text)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/index')
def index():
    return render_template('index.html') #THESE ARE JUST STATIC PAGES

if __name__ == "__main__":
    app.run()