# curriculos

<!-- 
Venv
sudo apt install python3-venv

Pip3
sudo apt install python3-pip

Pipenv
sudo apt install pipenv

Criar o ambiente na 1ª vez
pipenv --three

Entrar no ambiente
pipenv shell

Sair do ambiente
exit

Instalar individualmente os pacotes
pipenv install Flask

Instalar todo os pacotes
pipenv install

Aula 2
Configurando o banco de dados
sudo mysql -u root -p create database curriculos; create user 'suporte'@'localhost' identified by 'SuportE99'; grant all privileges on curriculos.* to 'suporte'@'localhost';

Criar o model
Configurar a aplicação
Configurar o Migration
Para inicializar o migrates (rodar somente 1 vez)
python3 migrations.py db init

Ao alterar algum dos models
python3 migrations.py db migrate python3 migrations.py db upgrade

CRUD (console interativo)
from app import db from app.models.tables import Usuario import bcrypt

Adicionar um novo usuário
senha_plana = 'Suporte99' senha_encriptada = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt()) u1 = Usuario(nome='Marco', email='marco@gmail.com', senha=senha_encriptada) db.session.add(u1) db.session.commit()

Selecionar todos os usuários
lista = Usuario.query.all()

Selecionar um usuário pelo ID
u2 = Usuario.query.filter_by(id=1).first() u2.email = 'marco.andrade@gmail.com' db.session.add(u2) db.session.commit()

Deletar um usuário
u3 = Usuario.query.filter_by(id=1).first() db.session.delete(u3) db.session.commit() 
-->