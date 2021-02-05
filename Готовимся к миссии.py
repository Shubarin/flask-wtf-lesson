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


@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    proffessions = [
        'инженер-исследователь', 'пилот', 'строитель',
        'экзобиолог', 'врач', 'инженер по терраформированию',
        'климатолог', 'специалист по радиационной защите', 'астрогеолог',
        'гляциолог', 'инженер жизнеобеспечения', 'метеоролог',
        'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов'
    ]
    context = {
        'proffessions': proffessions,
        'list_type': list_type,
        'title': 'Список профессий'
    }
    return render_template('proffessions.html', **context)


if __name__ == '__main__':
    app.debug = True
    app.run(port=8080, host='localhost')
