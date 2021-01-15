from jinja2 import FileSystemLoader, Environment

env = Environment(loader = FileSystemLoader('templates'))
template = env.get_template('if.html')

data = {'x':-8}
disp_text = template.render(data)
print(disp_text)
