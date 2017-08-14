import os
from PasswordBot import create_app, db
from PasswordBot.models import Adjectives, Adverbs, Nouns, Verbs
from flask_script import Manager
from flask_script import Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(
        app=app,
        db=db,
        Adjectives=Adjectives,
        Adverbs=Adverbs,
        Nouns=Nouns,
        Verbs=Verbs)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()