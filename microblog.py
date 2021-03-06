from app import app, db, cli
from app.models import User, Post, Notification, Message


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'cli': cli,
            'Message': Message,
            'Notification': Notification}


if __name__ == '__main__':
    app.run(debug=True)
