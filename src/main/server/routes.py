from flask import request, jsonify, make_response
from ...main.server.server_flask import app
from ...view.register_person_view import RegisterPersonViews
from ...view.search_combination_view import SearchCombinationViews

@app.route("/register", methods=["POST"])
def register_person_route():
    register_route = RegisterPersonViews()
    
    http_response = register_route.register_person_view(request)
    
    response = make_response(jsonify(http_response["data"]), http_response["status_code"])
    return response

@app.route("/register/search_combination/", methods=["GET"])
def search_person_route():
    search_route = SearchCombinationViews()

    http_response = search_route.search_combination_views(request.args)

    print(f"http_response: {http_response}")

    return jsonify(http_response["data"]), http_response["status_code"]
