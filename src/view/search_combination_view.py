from cerberus import Validator
from src.validators.validate_search import validate_search_user_query_params
from src.controllers.search_combination_controller import SearchCombinationController
from src.error_handling.error_handler import error_handler_method
from src.error_handling.validation_error import ValidationError

class SearchCombinationViews:
    def search_combination_views(self, request_args):
        try:
            query_params = dict(request_args)
            validation_response = validate_search_user_query_params(query_params)
            if not validation_response["is_valid"]:
                raise ValidationError("Invalid query params: {}".format(validation_response["error"]))

            name_first = request_args.get("name_first")
            name_second = request_args.get("name_second")

            search_combination_controller = SearchCombinationController()
            search_result = search_combination_controller.check_combination(name_first, name_second)

            if "message" not in search_result or search_result["message"] is None:
                return {
                    "status_code": 500,
                    "data": None,
                    "error": "Invalid response from check_combination method."
                }

            return {
                "status_code": 200,
                "data": search_result,
                "success": True
            }

        except Exception as exception:
            return {
                "status_code": 500,
                "data": None,
                "error": str(exception)
            }
