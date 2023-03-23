from src.infra.repository.person_repository import PersonRepository

class RegisterPersonController:
    def __init__(self):
        self.db_repository = PersonRepository()

    def register_person_controller(self, name_user: str, zodiac_sign: str):
        return self.db_repository.insert(name_user, zodiac_sign)
