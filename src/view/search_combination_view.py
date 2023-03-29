from cerberus import Validator
from src.validators.validate_search import validate_search_user_query_params
from src.controllers.search_combination_controller import SearchCombinationController
from src.error_handling.error_handler import error_handler_method
from src.error_handling.validation_error import ValidationError

class SearchCombinationViews:
    # Método para tratar a requisição da rota e retornar a resposta da pesquisa de combinação de signos
    def search_combination_views(self, request_args):
        try:
            # Converte os argumentos da requisição em um dicionário
            query_params = dict(request_args)
            
            # Valida os parâmetros de consulta recebidos
            validation_response = validate_search_user_query_params(query_params)
            if not validation_response["is_valid"]:
                raise ValidationError("Invalid query params: {}".format(validation_response["error"]))

            # Obtém os nomes das pessoas a partir dos parâmetros de consulta
            name_first = request_args.get("name_first")
            name_second = request_args.get("name_second")

            # Cria uma instância do controlador de pesquisa de combinação e verifica a compatibilidade dos signos
            search_combination_controller = SearchCombinationController()
            search_result = search_combination_controller.check_combination(name_first, name_second)

            # Verifica se a mensagem está presente no resultado da pesquisa e se não é None
            if "message" not in search_result or search_result["message"] is None:
                return {
                    "status_code": 500,
                    "data": None,
                    "error": "Invalid response from check_combination method."
                }

            # Retorna a resposta bem-sucedida com os dados da pesquisa de combinação
            return {
                "status_code": 200,
                "data": search_result,
                "success": True
            }
            
        except Exception as e:
            # Registre o erro e retorne um dicionário com uma mensagem de erro e um código de status de erro
            print(f"Erro ao registrar a pessoa: {e}")
            return {"data": {"error": "Ocorreu um erro ao registrar a pessoa."}, "status_code": 500}    
