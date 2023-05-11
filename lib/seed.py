#!/usr/bin/env python3

from random import choice as rc

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
from models import Audition, Role


engine = create_engine('sqlite:///production.db')
Session = sessionmaker(bind=engine)
session = Session()



def delete_records():
    session.query(Audition).delete()
    session.query(Role).delete()
    session.commit()

def create_records():
    auditions = [
        Audition(
            actor = "Joe",
            location = "NY",
            phone= random.randint(0,9),
            hired= random.randint(0,1),
            role_id = random.randint(1,10)
        ) for i in range(20)]
    roles = [
        Role(
            character_name = "Billy"
        ) for i in range(10)]
    session.add_all(auditions + roles)
    session.commit()
    return auditions, roles

def relate_records(auditions, roles):
    for role in roles:
        role.auditions = rc(auditions)
        

    session.add_all(roles)
    session.commit()

if __name__ == '__main__':
    delete_records()
    auditions, roles = create_records()
    relate_records(auditions, roles)