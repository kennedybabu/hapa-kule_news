from app import create_app
from flask_script import Manager, Server
# from app.models import News

# creating an app instance
app = create_app('production')

manager = Manager(app)
manager.add_command('server', Server)


if __name__ == '__main__':
    manager.run()