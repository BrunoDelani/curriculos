from app import app
from flask import render_template

@app.route('/home')
def pagina_inicial():
    return render_template('index.html')