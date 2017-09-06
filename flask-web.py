from flask import Flask, render_template, request
from pygments import highlight
from pygments.lexers.python import PythonLexer
from pygments.formatters.html import HtmlFormatter



app = Flask(__name__)




@app.route('/')
def hello_world():
    # return 'Hello World!'
    # 123
    name = 'print("hello world")'
    return render_template('hello.html', name=name)


@app.route('/code', methods=['GET', 'POST'])
def code():
    code = request.form['code']

    code = highlight(code, PythonLexer(), HtmlFormatter())
    css = HtmlFormatter().get_style_defs('.highlight')
    return render_template('code.html', code=code, css=css)


if __name__ == '__main__':
    app.debug = True
    app.run()
