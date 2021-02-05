from flask import Flask, render_template
from werkzeug.utils import redirect

from forms import LoginForm
from settings import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


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


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    fields = {
        'Фамилия': 'Вини',
        'Имя': 'Пух',
        'Образования': 'среднее',
        'Профессия': 'медведь',
        'Пол': 'мужской',
        'Мотивация': 'Марсианский мёд',
        'Готов остаться на Марсе': 'да'
    }
    context = {
        'title': 'Анкета',
        'fields': fields
    }
    return render_template('auto_answer.html', **context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.debug = True
    app.run(port=8080, host='localhost')
