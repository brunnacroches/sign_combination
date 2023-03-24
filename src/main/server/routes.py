from flask import request, jsonify, make_response
from src.main.server.server_flask import app
from src.view.register_person_view import RegisterPersonViews
from src.view.search_combination_view import SearchCombinationViews

    #  a função jsonify. A função jsonify aceita apenas um argumento: 
    # um dicionário com os dados a serem convertidos em uma resposta JSON. 
    # entao como melhoria no codigo, e combinado os dados e o código de status 
    # em um único objeto de resposta. 
@app.route("/register", methods=["POST"])
def register_person_route():
    register_route = RegisterPersonViews()
    
    http_response = register_route.register_person_view(request)
    
    response = make_response(jsonify(http_response["data"], http_response["status_code"]))
    return response

@app.route("/register/search_combination/", methods=["GET"])
def search_person_route():
    search_route = SearchCombinationViews()

    http_response = search_route.search_combination_views(request.args)

    print(f"http_response: {http_response}")

    return jsonify(http_response["data"]), http_response["status_code"]
