from jinja2 import Environment, FileSystemLoader

# pass the directory containing the templates to the FileSystemLoader.
file_loader = FileSystemLoader('templates')
# load the environment.
env = Environment(loader=file_loader)

# we can load the template.
template = env.get_template('hello.html')

output = template.render(name='Taro', lang='Python')
print(output)
