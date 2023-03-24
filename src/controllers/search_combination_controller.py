from src.controllers.register_person_controller import RegisterPersonController
from src.infra.repository.person_repository import PersonRepository

class SearchCombinationController:
    def __init__(self):
        self.db_repository = PersonRepository()

    def _is_sign_compatible(self, sign_first:str, sign_second: str) -> bool:
        # 1- implementar a logica de compatibilidade entre os signos
        compatible_signs = {
            "Aries": ["Aries", "Leo", "Sagittarius"],
            "Taurus": ["Taurus", "Virgo", "Capricorn"],
            "Gemini": ["Gemini", "Libra", "Aquarius"],
            "Cancer": ["Cancer", "Scorpio", "Pisces"],
            "Leo": ["Aries", "Leo", "Sagittarius"],
            "Virgo": ["Taurus", "Virgo", "Capricorn"],
            "Libra": ["Gemini", "Libra", "Aquarius"],
            "Scorpio": ["Cancer", "Scorpio", "Pisces"],
            "Sagittarius": ["Aries", "Leo", "Sagittarius"],
            "Capricorn": ["Taurus", "Virgo", "Capricorn"],
            "Aquarius": ["Gemini", "Libra", "Aquarius"],
            "Pisces": ["Cancer", "Scorpio", "Pisces"]
        }

        # ! verificando se sing_second é compatível com sign_first
        if sign_first not in compatible_signs:
            print(f"sign_first ({sign_first}) not found in compatible_signs: {compatible_signs}")
            return False

        return sign_second in compatible_signs[sign_first]
    
    def check_combination(self, name_first: str, name_second: str) -> dict:
        person_first = self.db_repository.find_by_name(name_first)
        person_second = self.db_repository.find_by_name(name_second)

        print(f"Person 1: {person_first}")
        print(f"Person 2: {person_second}")

        if person_first is None or person_second is None:
            return {
                "message": "One or both of the users were not found."
            }

        sign_first = person_first.zodiac_sign
        sign_second = person_second.zodiac_sign

        print(f"Sign 1: {sign_first}")
        print(f"Sign 2: {sign_second}")

        is_compatible = self._is_sign_compatible(sign_first, sign_second)

        result = {
            "message": "Signs are compatible." if is_compatible else "Signs are not compatible."
        }

        print(f"check_combination result: {result}")

        return result
