from src.main.server.server_flask import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# http://localhost:5000/register/search_combination/?name_first=Jonny&name_second=Jana