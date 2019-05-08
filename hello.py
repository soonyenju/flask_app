from flask import Flask, request, abort, redirect, url_for, render_template
from jinja2 import Template
from markdown import markdown
from pathlib import Path

app = Flask(__name__, template_folder = "tempalte", static_folder = "static")

# app.config["DEBUG"] = True
app.config.from_object("settings")

template = Template("Hello {{name}}")

@app.route('/')
def hello_world():
    Dict = {
        "content": "Songyan",
        "items": [
            {
                "href": "md",
                "caption": "mds"
            },
            {
                "href": "articles",
                "caption": "articles"
            }
        ]
    }
    return render_template("index.html", **Dict)

@app.route('/articles/')
def article_list():

    arti_dict = {
        "items":[
        ]
    }

    md_paths = Path(app.static_folder).joinpath("sources").glob(r"*.md")
    for i, p in enumerate(md_paths):
        print(p)
        arti_dict["items"].append({
            "href": f"The {i} article",
            "caption": p
            })

    # return template.render(name = "songyan")
    return render_template("articles.html", **arti_dict)

@app.route("/articles/<id>")
def article(id):
    return f"{id}"

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