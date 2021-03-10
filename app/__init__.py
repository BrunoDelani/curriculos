from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://suporte:SuportE99@localhost/curriculos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.models.tables import Usuario

from app.controllers import usuarios
from app.controllers import instituicoes
from app.controllers import home
from app.controllers import formacaoAcademica
from app.controllers import formacaoComplementar
from app.controllers import cursos
from app.controllers import atuacaoProfissional
from app.controllers import atividadeProfissional
