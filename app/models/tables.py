from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200))
    email = db.Column(db.String(200), index=True, unique=True)
    senha = db.Column(db.String(200))
    admin = db.Column(db.Boolean())

    def __repr__(self):
        return '<Usuario %s>' % self.nome


class Instituicao(db.Model):
    __tablename__ = 'instituicoes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    sigla = db.Column(db.String(20))

    def __repr__(self):
        return '<Instituição %s>' % self.nome


class Curso(db.Model):
    __tablename__ = 'cursos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    instituicao_id = db.Column(db.Integer, db.ForeignKey('instituicoes.id'), nullable=False)

    def __repr__(self):
        return '<Curso %s>' % self.nome


class FormacaoAcademica(db.Model):
    __tablename__ = 'formacoes_academicas'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'), nullable=False)
    trabalho_conclusao = db.Column(db.String(200), nullable=False)
    inicio = db.Column(db.Date(), nullable=False)
    termino = db.Column(db.Date())

    def __repr__(self):
        return '<Formação Acadêmica %s>' % self.trabalho_conclusao.nome


class FormacaoComplementar(db.Model):
    __tablename__ = 'formacoes_complementares'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    instituicao_id = db.Column(db.Integer, db.ForeignKey('instituicoes.id'), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    inicio = db.Column(db.Date(), nullable=False)
    termino = db.Column(db.Date())

    def __repr__(self):
        return '<Formação Complementar %s>' % self.descricao


class AtuacaoProfissional(db.Model):
    __tablename__ = 'atuacoes_profissionais'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    instituicao_id = db.Column(db.Integer, db.ForeignKey('instituicoes.id'), nullable=False)
    inicio = db.Column(db.Date(), nullable=False)
    termino = db.Column(db.Date())
    
    def __repr__(self):
        return '<Atuação Profissional %s>' % self.instituicao_id


class AtividadeProfissional(db.Model):
    __tablename__ = 'atividades_profissionais'

    id = db.Column(db.Integer, primary_key=True)
    atuacao_profissional_id = db.Column(db.Integer, db.ForeignKey('atuacoes_profissionais.id'), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    inicio = db.Column(db.Date(), nullable=False)
    termino = db.Column(db.Date())    
    
    def __repr__(self):
        return '<Atividades Profissionais %s>' % self.descricao