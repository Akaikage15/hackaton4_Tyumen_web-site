import json
from datetime import datetime
import hashlib
import os

from flask import Flask, request, render_template, redirect, url_for
#from flask_login import LoginManager, login_user, login_required, current_user
from flask_migrate import Migrate

from models import *
from forms import *
from database import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SECRET_KEY"] = "I LOVE PYTHON"
db.init_app(app)
migrate = Migrate(app, db)
#login_manager = LoginManager(app)

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/quests')
def quests_list():
    quests = db.session.query(Quests).all()
    return render_template('quests_list.html', quests=quests)


@app.route('/quests/get', methods=['GET'])
def quests():

    def clear_quests(quests):
        return {'dete': quests.date, 'id': quests.id, 'name': quests.name}

    quests = db.session.query(Quests).all()
    quests = list(map(clear_quests, quests))
    print(quests)

    return json.dumps(quests), 200
    #return render_template('quest.html')


@app.route('/quests/get/<id>', methods=['GET'])
def quests_get_id(id):

    quests = db.get_or_404(Quests, id)
    result = {'dete': quests.date, 'id': quests.id, 'name': quests.name}

    return json.dumps(result), 200

@app.route('/gastronomy/create', methods=['GET', 'POST'])
def gastronomy_create():
    if request.method == 'GET':
        form = CreateGastronomy()
        return render_template('create_gastronomy.html', form=form)
    elif request.method == 'POST':
        name = request.form.get('name')
        text = request.form.get('text')
        file = request.files.get('img')

        file.save(os.path.join('static/img/', file.filename))
        img = os.path.join('../static/img/', file.filename)

        new_gastronomy = Gastronomy(name=name, img=img, text=text, )

        db.session.add(new_gastronomy)
        db.session.commit()
        db.session.flush()

        id = new_gastronomy.id

        return json.dumps({'id': id}), 200


@app.route('/quests/create', methods=['GET', 'POST'])
def create_quests():
    if request.method == 'GET':
        form = CreateQuests()
        return render_template('create_quests.html', form=form)
    elif request.method == 'POST':
        name = request.form.get('name')
        date = request.form.get('date')

        new_quest = Quests(name=name, date=date)

        db.session.add(new_quest)
        db.session.commit()
        db.session.flush()

        id = new_quest.id

        return json.dumps({'id': id}), 200


@app.route('/history')
def history():
    return render_template('history_page.html')


@app.route('/historyQuiz')
def hictory_Quiz():
    return render_template('history_Quiz.html')


@app.route('/facts')
def facts():
    return render_template('facts.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/culture')
def culture():
    return render_template('culture.html')


@app.route('/gastronomy')
def gastronomy():
    data_gastronomy = db.session.query(Gastronomy).all()
    return render_template('gastronomy.html', data_gastronomy=data_gastronomy)


@app.route('/pashalko')
def pashalko():
    return render_template('pashalko.html')


if __name__ == "__main__":
    app.run(debug=True)