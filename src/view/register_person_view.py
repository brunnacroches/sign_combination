from cerberus import Validator
from ..validators.validate_register import validate_register_user_request_body
from ..controllers.register_person_controller import RegisterPersonController
from ..error_handling.validation_error import ValidationError
from ..error_handling.error_handler import error_handler_method

class RegisterPersonViews:
    def register_person_view(self, request):
        try:
            validation_response = validate_register_user_request_body(request.json)
            if not validation_response["is_valid"]:
                raise ValidationError("Invalid request body", validation_response["error"])
            
            body = request.json
            name_user = body["name_user"]
            zodiac_sign = body["zodiac_sign"]

            # chama o controller para criar o registro
            register_person_controller = RegisterPersonController()
            register_person_controller.register_person_controller(name_user, zodiac_sign)
            
            return {
                "status_code": 200,
                "data": {
                    "name_user": name_user,
                    "zodiac_sign": zodiac_sign
                },
                "success": True
            }
            

        except Exception as e:
            # Registre o erro e retorne um dicionário com uma mensagem de erro e um código de status de erro
            print(f"Erro ao registrar a pessoa: {e}")
            return {"data": {"error": "Ocorreu um erro ao registrar a pessoa."}, "status_code": 500}    