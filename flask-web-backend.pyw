from flask import Flask, render_template, request
from pygments import highlight
from pygments.lexers.python import PythonLexer
from pygments.formatters.html import HtmlFormatter
from pygments.styles import get_all_styles, STYLE_MAP,get_style_by_name
from pygments.lexers import get_lexer_by_name
import time
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/code', methods=['GET', 'POST'])
def code():
    try:
        code = request.form['code']
        stylename = request.form['style']
        lang = request.form['lang']
    except:
        code = ''
        stylename = 'igor'
        lang = 'python'

    if stylename == '' or stylename is None or stylename == '代码高亮':
        stylename = 'igor'
    if lang == '' or lang is None:
        lang = 'python'

    style_list = get_all_styles()
    style = get_style_by_name(stylename)
    if code:
        lexer = get_lexer_by_name(lang)
        formatter = HtmlFormatter(style=style, cssclass='syntax', linenos=False)
        highlightcode = highlight(code, lexer, formatter)
        highlightcss = formatter.get_style_defs('.syntax pre')
    else:
        highlightcode = ''
        highlightcss = ''

    return render_template('code.html', code=code, highlightcss=highlightcss, highlightcode=highlightcode,
                           style_list=style_list, style=stylename, lang=lang)



@app.route('/time', methods=['GET', 'POST'])
def timestamp():
    now = int(time.time())
    sj = datetime.datetime.now()
    return render_template('timestamp.html', now=now, sj=sj)

if __name__ == '__main__':
    app.debug = True
    app.run()
