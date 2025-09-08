from models.base import Session, init_db
from models.user import User

init_db()
session = Session()

if session.query(User).count() == 0:
    users = [User(name='João'), User(name='Maria'), User(name='Ana')]
    session.add_all(users)
    session.commit()
    print("Usuários adicionados.")
else:
    print("Usuários já existem.")
