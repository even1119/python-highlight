from pygments import highlight
from pygments.lexers.python import PythonLexer
from pygments.formatters.html import HtmlFormatter



code = 'print "Hello World"'

print(highlight(code, PythonLexer(), HtmlFormatter()))
css = HtmlFormatter().get_style_defs('.highlight')
print(css)