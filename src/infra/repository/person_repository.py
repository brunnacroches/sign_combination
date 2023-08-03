from ...infra.entities.person_entities import Person

class PersonRepository:
    def __init__(self, ConnectionHandler) -> None:
        self.__ConnectionHandler = ConnectionHandler

    def select(self):
        with self.__ConnectionHandler() as db:
            try:
                data = db.session.query(Person).all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, name_user: str, zodiac_sign: str) -> Person:
        with self.__ConnectionHandler() as db:
            try:
                data_insert = Person(
                    name_user=name_user,
                    zodiac_sign=zodiac_sign
                )
                db.session.add(data_insert) 
                db.session.commit()
                return data_insert
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, id_user: int):
        with self.__ConnectionHandler() as db:
            try:
                deleted_rows = db.session.query(Person).filter(
                    Person.id_user == id_user
                ).delete()
                db.session.commit()
                if deleted_rows > 0:
                    return id_user
                else:
                    return None  # Ou você pode levantar uma exceção aqui, dependendo da sua lógica de negócio
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, id_user:int, new_id_user: int):
        with self.__ConnectionHandler() as db:
            try:
                db.session.query(Person).filter(
                    Person.id_user == id_user
                ).update(
                    {"id_user": new_id_user}
                )
                db.session.commit()
                return new_id_user
            except Exception as exception:
                db.session.rollback()
                raise exception

    def find_by_name(self, name_user: str) -> Person:
        with self.__ConnectionHandler() as db:
            try:
                person = db.session.query(Person).filter(
                    Person.name_user == name_user
                ).one_or_none()
                print(f"find_by_name result for {name_user}: {person}")
                return person
            except Exception as exception:
                db.session.rollback()
                raise exception
