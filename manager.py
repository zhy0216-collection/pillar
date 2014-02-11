from flask.ext.script import Manager
from web.app import app

manager = Manager(app)

@manager.command
def hello():
    return "hello"


if __name__ == "__main__":
    manager.run()