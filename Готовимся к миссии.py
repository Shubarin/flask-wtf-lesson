from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/<title>')
@app.route('/index/<title>')
def index(title='Главная'):
    return render_template('base.html', title=title)


if __name__ == '__main__':
    app.debug = True
    app.run(port=8080, host='localhost')
