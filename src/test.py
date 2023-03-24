from src.infra.repository.person_repository import PersonRepository

def test_find_by_name():
    repo = PersonRepository()
    name_first = "Joao"  
    name_second = "Fabiana"

    person_first = repo.find_by_name(name_first)
    person_second = repo.find_by_name(name_second)

    print("person_first:", person_first)
    print("person_second:", person_second)

if __name__ == "__main__":
    test_find_by_name()
