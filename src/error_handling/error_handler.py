from src.error_handling.validation_error import ValidationError

def error_handler_method(error):
    if isinstance(error, ValidationError):
        print("Handle my custom error")
        return {
            "status_code": 400,
            "data": error.message
        }

    if isinstance(error, ZeroDivisionError):
        print('Treat division by zero')
        return {
            "status_code": 400,
            "data": "Division by zero is not allowed"
        }

    # if isinstance(error, Exception):
    #     print('Treat general case')
    #     return {
    #         "status_code": 500,
    #         "data": 'An unexpected error occurred'
    #     }
