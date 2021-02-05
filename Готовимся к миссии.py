from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/<title>')
@app.route('/index/<title>')
def index(title='Главная'):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof or 'строитель' in prof:
        text = 'Инженерный тренажер'
    else:
        text = 'Научный тренажер'
    context = {
        'title': 'Тренировка',
        'text': text
    }
    return render_template('training.html', **context)


if __name__ == '__main__':
    app.debug = True
    app.run(port=8080, host='localhost')
