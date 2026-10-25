from flask import Flask
from model.models import db
from view.routes import rotas

app = Flask(__name__)
app.config['SECRET_KEY'] = "minha_chave_123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Agendas.db'

db.init_app(app)
app.register_blueprint(rotas)

if __name__ == '__main__':
    app.run(debug=True)