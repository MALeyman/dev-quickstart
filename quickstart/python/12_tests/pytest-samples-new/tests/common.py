from sqlalchemy import orm

'''
Импортирует scoped_session и sessionmaker из SQLAlchemy ORM
scoped_session обеспечивает управление жизненным циклом сессий в многопоточной среде.
sessionmaker() позволяет настраивать параметры сессии (например, соединение с базой данных).
'''
Session = orm.scoped_session(orm.sessionmaker())
