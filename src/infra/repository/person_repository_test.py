import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from unittest import mock
from unittest.mock import MagicMock, patch
from ...infra.entities.person_entities import Person
from ...infra.repository.person_repository import PersonRepository
import os

os.environ["SQLALCHEMY_WARN_20"] = "1"

class ConnectionHandlerMock:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [
                        mock.call.query(Person),  # condição para acessar esses dados
                    ],
                    [Person(id_user=1234, name_user="Fabiana", zodiac_sign="Aries")]
                )
            ]
        )

    # Método especial __enter__ é chamado ao entrar em um bloco 'with'
    def __enter__(self):
        return self

    # Método especial __exit__ é chamado ao sair do bloco 'with'
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Fechando a sessão atual
        self.session.close()

    def __call__(self):
        return self

    # Método especial __enter__ é chamado ao entrar em um bloco 'with'
    def __enter__(self):
        return self

    # Método especial __exit__ é chamado ao sair do bloco 'with'
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Fechando a sessão atual
        self.session.close()


def test_select():
    person_repository = PersonRepository(ConnectionHandlerMock)
    response = person_repository.select()
    print()
    print(response)
    assert isinstance(response, list)
    assert isinstance(response[0], Person)
    assert response[0].name_user == "Fabiana"

def test_insert():
    person_repository = PersonRepository(ConnectionHandlerMock)
    response = person_repository.insert("Joana", "Pisces")
    print()
    print(response)
    assert isinstance(response, Person)

def test_delete():
    person_repository = PersonRepository(ConnectionHandlerMock)
    response = person_repository.delete(1234)
    print()
    print(response)
    assert response == 1234

def test_update():
    person_repository = PersonRepository(ConnectionHandlerMock)
    response = person_repository.update(1234, 4321)
    print()
    print(response)
    assert response == 4321

def test_find_by_name():
    person_repository = PersonRepository(ConnectionHandlerMock)
    response = person_repository.find_by_name("Fabiana")
    print()
    print(response)
    assert response.name_user == "Fabiana"
