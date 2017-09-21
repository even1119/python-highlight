from flask import Flask, render_template, request
from pygments import highlight
from pygments.lexers.python import PythonLexer
from pygments.formatters.html import HtmlFormatter



app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/code', methods=['GET', 'POST'])
def code():
    code = request.form['code']

    code = highlight(code, PythonLexer(), HtmlFormatter())
    css = HtmlFormatter().get_style_defs('.highlight')
    return render_template('code.html', code=code, css=css)


# 运行主程序
if __name__ == '__main__':
    app.debug = True
    app.run()
