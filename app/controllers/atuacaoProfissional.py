from app import app
from flask import render_template
from app.models.tables import AtuacaoProfissional
from app.models.tables import Instituicao
from app.models.tables import Usuario

@app.route('/atuacaoProfissional')
def listar_atuacoesProfissionais():
    a = AtuacaoProfissional.query.all()
    i = Instituicao.query.all()
    u = Usuario.query.all()
    return render_template('atuacaoProfissional.html', atuacao_profissional = a, instituicao = i, usuario = u)