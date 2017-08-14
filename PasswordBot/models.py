from PasswordBot import db
import random

class Words(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    word = db.Column(db.String(255), nullable=False)
    ipm = db.Column(db.Float, nullable=False)
    rang = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        '''presentation output'''
        return "Word: '{}', freq: '{}', rang '{}'".format(
            self.word,
            self.ipm,
            self.rang
            )

    def __init__(self, word, ipm, rang):
        '''init data row in table'''
        self.word = word
        self.ipm = ipm
        self.rang = rang

class Verbs(Words):
    __tablename__ = 'Verbs'


class Adverbs(Words):
    __tablename__ = 'Adverbs'


class Adjectives(Words):
    __tablename__ = 'Adjectives'


class Nouns(Words):
    __tablename__ = 'Nouns'
