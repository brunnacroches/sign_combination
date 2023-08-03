from cerberus import Validator
from ..error_handling.validation_error import ValidationError

def validate_search_user_query_params(query_params):
    schema = {
        "name_first": {"type": "string", "required": True},
        "name_second": {"type": "string", "required": True}
    }
    validator = Validator(schema)
    is_valid = validator.validate(query_params)
    
    if not is_valid:
        raise ValidationError({"message": "Invalid request body", "errors": validator.errors})

    return {
        "is_valid": is_valid,
        "error": validator.errors
    }