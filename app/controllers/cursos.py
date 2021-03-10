from app import app
from flask import render_template
from app.models.tables import Curso
from app.models.tables import Instituicao

@app.route('/cursos')
def listar_cursos():
    c = Curso.query.all()
    i = Instituicao.query.all()
    return render_template('cursos.html', curso = c, instituicao = i)