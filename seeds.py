from app import db
from app.models.tables import Usuario, Instituicao, Curso, AtuacaoProfissional, AtividadeProfissional, FormacaoAcademica, FormacaoComplementar
import bcrypt
import datetime

# Criando usuários
senha_plana = '45@78@12'
senha_encriptada = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt())
u1 = Usuario(nome='Pedro', email='pedroluisfbar@gmail.com', senha=senha_encriptada)
db.session.add(u1)
senha_plana = '12@45@78'
senha_encriptada = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt())
u2 = Usuario(nome='Bruno', email='br.delani@gmail.com', senha=senha_encriptada)
db.session.add(u2)
senha_plana = '78@12@45'
senha_encriptada = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt())
u3 = Usuario(nome='João', email='jvlaaa@gmail.com', senha=senha_encriptada)
db.session.add(u3)
db.session.commit()

# Criando Instituições
i1 = Instituicao(nome='Instituto Federal de Rondônia', sigla='IFRO')
i2 = Instituicao(nome='Serviço Nacional de Aprendizagem', sigla='SENAI')
i3 = Instituicao(nome='Serviço Social da Indústria', sigla='SESI')
i4 = Instituicao(nome='Masutti')
i5 = Instituicao(nome='Polícia Federal', sigla="PF")
i6 = Instituicao(nome='Secrataria Municipal de Educação', sigla='SEMED')
i7 = Instituicao(nome='Escola Vanks', sigla='Vanks')
db.session.add(i1)
db.session.add(i2)
db.session.add(i3)
db.session.add(i4)
db.session.add(i5)
db.session.add(i6)
db.session.add(i7)
db.session.commit()

# Criando Cursos
inst = Instituicao.query.filter_by(sigla='SESI').first()
c1 = Curso(nome='Fundamental I', instituicao_id=inst.id)
c2 = Curso(nome='Fundamental II', instituicao_id=inst.id)
inst = Instituicao.query.filter_by(sigla='IFRO').first()
c3 = Curso(nome='Técnico em Informática integrado ao Ensino Médio', instituicao_id=inst.id)
c4 = Curso(nome='CSD em Análise e Desenvolvimento de Software', instituicao_id=inst.id)
inst = Instituicao.query.filter_by(sigla='Vanks').first()
c5 = Curso(nome='Fundamental I', instituicao_id=inst.id)
c6 = Curso(nome='Fundamental II', instituicao_id=inst.id)
db.session.add(c1)
db.session.add(c2)
db.session.add(c3)
db.session.add(c4)
db.session.add(c5)
db.session.add(c6)
db.session.commit()

# Criando atuações profissionais
us = Usuario.query.filter_by(nome="Pedro").first()
ins = Instituicao.query.filter_by(nome="Masutti").first()
atuaProf1 = AtuacaoProfissional(usuario_id=us.id, instituicao_id=ins.id, inicio=datetime.datetime(2018, 5, 17), termino=datetime.datetime(2018, 7, 17))
db.session.add(atuaProf1)

us = Usuario.query.filter_by(nome="Bruno").first()
ins = Instituicao.query.filter_by(sigla="SEMED").first()
atuaProf2 = AtuacaoProfissional(usuario_id=us.id, instituicao_id=ins.id, inicio=datetime.datetime(2018, 3, 15), termino=datetime.datetime(2018, 5, 15))
db.session.add(atuaProf2)

us = Usuario.query.filter_by(nome="João").first()
ins = Instituicao.query.filter_by(sigla="PF").first()
atuaProf2 = AtuacaoProfissional(usuario_id=us.id, instituicao_id=ins.id, inicio=datetime.datetime(2020, 7, 7))
db.session.add(atuaProf2)

db.session.commit()

# Criando atividade profissional
atuaProf = AtuacaoProfissional.query.get(1)
ativProf1 = AtividadeProfissional(atuacao_profissional_id=atuaProf.id, descricao="Estágio", inicio=datetime.datetime(2018, 5, 17), termino=datetime.datetime(2018, 7, 17))
db.session.add(ativProf1)

atuaProf = AtuacaoProfissional.query.get(2)
ativProf2= AtividadeProfissional(atuacao_profissional_id=atuaProf.id, descricao="Estágio", inicio=datetime.datetime(2018, 3, 15), termino=datetime.datetime(2018, 5, 15))
db.session.add(ativProf2)

atuaProf = AtuacaoProfissional.query.get(3)
ativProf3 = AtividadeProfissional(atuacao_profissional_id=atuaProf.id, descricao="Estágio", inicio=datetime.datetime(2020, 7, 7))
db.session.add(ativProf3)

db.session.commit()

# Criando formações acadêmicas
cur = Curso.query.filter_by(nome="Fundamental I").first()
usr = Usuario.query.filter_by(nome="Pedro").first()
frmAca1 = FormacaoAcademica(usuario_id=usr.id, curso_id=cur.id, trabalho_conclusao="Aprovado por nota", inicio=datetime.datetime(2007, 3, 19), termino=datetime.datetime(2012, 11, 30))
usr = Usuario.query.filter_by(nome="Bruno").first()
frmAca2 = FormacaoAcademica(usuario_id=usr.id, curso_id=cur.id, trabalho_conclusao="Aprovado por nota", inicio=datetime.datetime(2007, 3, 19), termino=datetime.datetime(2012, 11, 30))
usr = Usuario.query.filter_by(nome="João").first()
frmAca3 = FormacaoAcademica(usuario_id=usr.id, curso_id=cur.id, trabalho_conclusao="Aprovado por nota", inicio=datetime.datetime(2007, 3, 19), termino=datetime.datetime(2012, 11, 30))
db.session.add(frmAca1)
db.session.add(frmAca2)
db.session.add(frmAca3)

cur = Curso.query.filter_by(nome="Fundamental II").first()
usr = Usuario.query.filter_by(nome="Pedro").first()
frmAca4 = FormacaoAcademica(usuario_id=usr.id, curso_id=cur.id, trabalho_conclusao="Aprovado por nota", inicio=datetime.datetime(2013, 3, 20), termino=datetime.datetime(2015, 11, 29))
usr = Usuario.query.filter_by(nome="Bruno").first()
frmAca5 = FormacaoAcademica(usuario_id=usr.id, curso_id=cur.id, trabalho_conclusao="Aprovado por nota", inicio=datetime.datetime(2013, 3, 20), termino=datetime.datetime(2015, 11, 29))
db.session.add(frmAca4)
db.session.add(frmAca5)

cur = Curso.query.filter_by(nome="Técnico em Informática integrado ao Ensino Médio").first()
usr = Usuario.query.filter_by(nome="Pedro").first()
frmAca6 = FormacaoAcademica(usuario_id=usr.id, curso_id=cur.id, trabalho_conclusao="Relatório de estágio", inicio=datetime.datetime(2016, 4, 16), termino=datetime.datetime(2018, 12, 10))
usr = Usuario.query.filter_by(nome="Bruno").first()
frmAca7 = FormacaoAcademica(usuario_id=usr.id, curso_id=cur.id, trabalho_conclusao="Relatório de estágio", inicio=datetime.datetime(2016, 4, 16), termino=datetime.datetime(2018, 12, 10))
usr = Usuario.query.filter_by(nome="João").first()
frmAca8 = FormacaoAcademica(usuario_id=usr.id, curso_id=cur.id, trabalho_conclusao="Relatório de estágio", inicio=datetime.datetime(2016, 4, 16), termino=datetime.datetime(2018, 12, 10))
db.session.add(frmAca6)
db.session.add(frmAca7)
db.session.add(frmAca8)

cur = Curso.query.filter_by(nome="CSD em Análise e Desenvolvimento de Software").first()
usr = Usuario.query.filter_by(nome="Pedro").first()
frmAca9 = FormacaoAcademica(usuario_id=usr.id, curso_id=cur.id, trabalho_conclusao="Caixa agro", inicio=datetime.datetime(2019, 3, 28))
usr = Usuario.query.filter_by(nome="Bruno").first()
frmAca10 = FormacaoAcademica(usuario_id=usr.id, curso_id=cur.id, trabalho_conclusao="Gerência TI", inicio=datetime.datetime(2019, 3, 28))
usr = Usuario.query.filter_by(nome="João").first()
frmAca11 = FormacaoAcademica(usuario_id=usr.id, curso_id=cur.id, trabalho_conclusao="Curso 3D", inicio=datetime.datetime(2019, 3, 28))
db.session.add(frmAca9)
db.session.add(frmAca10)
db.session.add(frmAca11)

db.session.commit()

# Criando formações complementares
ins = Instituicao.query.filter_by(sigla="IFRO").first()
usr = Usuario.query.filter_by(nome="Pedro").first()
formComp1 = FormacaoComplementar(usuario_id=usr.id, instituicao_id=ins.id, descricao="Oficina de desenvolvimento WEB", inicio=datetime.datetime(2017, 10, 8), termino=datetime.datetime(2017, 10, 10))
db.session.add(formComp1)

formComp2 = FormacaoComplementar(usuario_id=usr.id, instituicao_id=ins.id, descricao="Oficina de impressão 3D", inicio=datetime.datetime(2017, 10, 11), termino=datetime.datetime(2017, 10, 11))
db.session.add(formComp2)

usr = Usuario.query.filter_by(nome="João").first()
formComp3 = FormacaoComplementar(usuario_id=usr.id, instituicao_id=ins.id, descricao="Oficina de impressão 3D", inicio=datetime.datetime(2017, 10, 11), termino=datetime.datetime(2017, 10, 11))
db.session.add(formComp3)

usr = Usuario.query.filter_by(nome="Bruno").first()
formComp3 = FormacaoComplementar(usuario_id=usr.id, instituicao_id=ins.id, descricao="Oficina de impressão 3D", inicio=datetime.datetime(2017, 10, 11), termino=datetime.datetime(2017, 10, 11))
db.session.add(formComp3)

db.session.commit()