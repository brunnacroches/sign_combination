from src.infra.configs.connection import DBConnectionHandler
from src.infra.entities.person_entities import Person

class PersonRepository:
    def select(self):
        try:
            with DBConnectionHandler() as db:
                data = db.session.query(Person).all()
                return data
        except Exception as e:
            print(f'Error selecting person {str(e)}')
            return None

    def insert(self, name_user: str, zodiac_sign: str) -> Person:
        try:
            with DBConnectionHandler() as db:
                data_insert = Person(
                    name_user=name_user,
                    zodiac_sign=zodiac_sign
                )
                db.session.add(data_insert) 
                db.session.commit()
                return data_insert
        except Exception as e:
            print(f'Error inserting person {str(e)}')
            db.session.rollback()
            return None

    def delete(self, id_user: int):
        try:
            with DBConnectionHandler() as db:
                db.session.query(Person).filter(
                    Person.id_user == id_user
                ).delete()
                db.session.commit()
        except Exception as e:
            print(f'Error delete person {str(e)}')
            return None

    def update(self, id_user:int, new_id_user: int):
        try:
            with DBConnectionHandler() as db:
                db.session.query(Person).filter(
                    Person.id_user == id_user
                ).update(
                    {"id_user": new_id_user}
                )
                db.session.commit()
        except Exception as e:
            print(f'Error update person {str(e)}')
            return None

    def find_by_name(self, name_user: str) -> Person:
        try:
            with DBConnectionHandler() as db:
                person = db.session.query(Person).filter(
                    Person.name_user == name_user
                ).one_or_none()
                return person
        except Exception as e:
            print(f'Error finding person by name {str(e)}')
            return None
