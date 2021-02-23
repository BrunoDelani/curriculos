from flask import Flask
from flask import render_template 

app = Flask(__name__)


@app.route('/home')
def home():
    l = ['Programador','Manutenção','Marketing', 'Suporte']
    return render_template('index.html', lista=l)
