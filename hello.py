from flask import Flask, request, abort, redirect, url_for, render_template
from jinja2 import Template
from markdown import markdown

app = Flask(__name__, template_folder = "./public")

# app.config["DEBUG"] = True
app.config.from_object("settings")

template = Template("Hello {{name}}")

@app.route('/')
def hello_world():
    Dict = {
        "content": "jojo",
        "items": [
            {
                "href": "baidu",
                "caption": "search engine"
            }
        ]
    }
    return render_template("index.html", **Dict)

@app.route('/code/')
def mycode():
    return template.render(name = "songyan")

@app.route('/md/')
def parse_md():
    markDown_text = "good"
    with open("text.md", 'r', encoding='utf-8') as f:
        markDown_text = f.read()
    html_text = markdown(markDown_text, output_format = 'html')
    return html_text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)

'''
if no main(), use following code snippet:
set FLASK_APP=hello.py
python -m flask run
'''