from flask import Flask


app = Flask(__name__)

app.config.update(
    SECRET_KEY='abc123',
    TEMPLATES_AUTO_RELOAD=True
)


@app.route('/')
def index():
    return """<h1>The Application Works!</h1>
    <img src='/static/image/image.jpg' width='150'/>"""
