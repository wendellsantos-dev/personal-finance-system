from datetime import datetime, timezone
from app import db

class User(db.Model):
    __tablename__ = "users" 
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    senha_hash = db.Column(db.String(255), nullable = False)
    data_criacao = db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc))

    class Transaction(db.Model):
        __tablename__ = 'transactions'
        id = db.Column(db.Integer, primary_key = True)
        descricao = db.Column(db.String(200), nullable = False)
        valor = db.Column(db.Float, nullable = False)
        tipo = db.Column(db.String(10), nullable = False)
        categoria = db.Column(db.String(50), nullable = False)
        data = db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc))
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

