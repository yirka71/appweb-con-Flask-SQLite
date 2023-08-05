
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# El engine permite a SQLAlchemy comunicarse con la base de datos, una BDD especifica
# https://docs.sqlalchemy.org/en/14/core/engines.html
engine = create_engine("sqlite:///database/tareas.db",connect_args={"check_same_thread":False})
#Le dice a sqlitealchemy a que motor de BDD se va a conectar, OracledB, sqlite, microsoft service
#mysqlite

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
