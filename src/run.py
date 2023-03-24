from src.main.server.server_flask import app
from flask import jsonify

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

@app.errorhandler(Exception)
def handle_exception(e):
    # log the error
    print(str(e))

    # return error message
    response = {
        "status_code": 500,
        "error": str(e)
    }
    return jsonify(response), 500
