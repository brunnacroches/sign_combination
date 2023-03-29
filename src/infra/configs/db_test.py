from src.infra.configs.connection import DBConnectionHandler
from src.infra.entities.person_entities import Person

def test_db_connection():
    connection_handler = DBConnectionHandler()
    
    with connection_handler as conn:
        session = conn.session
        try:
            # Substitua esta consulta de exemplo pela consulta adequada para o seu banco de dados
            result = session.query(Person).all()
            print("Resultado da consulta:", result)
        except Exception as e:
            print("Erro ao executar a consulta:", e)
        finally:
            session.close()

if __name__ == "__main__":
    test_db_connection()