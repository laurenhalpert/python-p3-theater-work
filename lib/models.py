from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)
class Role(Base):
    __tablename__="roles"

    

    id = Column(Integer(), primary_key=True)
    character_name = Column(String())

    auditions = relationship('Audition', backref='role')
    def actors(self):
        return [audition.actor for audition in self.auditions]
    def locations(self):
        return [audition.location for audition in self.auditions]
    def lead(self):
        if len(self.auditions) != 0:
            return self.auditions[0]
        else:
            return 'no actor has been hired for this role'
    def understudy(self):
        if len(self.auditions) >= 2:
            return self.auditions[1]
        else:
            return'no actor has been hired for understudy for this role'
    def __repr__(self):
        return f'<Role {self.character_name}'

class Audition(Base):
    __tablename__='auditions'

    id = Column(Integer(), primary_key=True)
    actor = Column(String())
    location = Column(String())
    phone= Column(Integer())
    hired= Column(Integer())
    role_id = Column(Integer(), ForeignKey('roles.id'))

    def call_back(self):
        self.hired = 1
    def __repr__(self):
        return f'<Audition {self.actor}'