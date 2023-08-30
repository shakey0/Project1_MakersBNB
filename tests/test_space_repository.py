from lib.space_repository import *
from lib.space import *

'''
When we call SpaceRepository #all method
We get a list of Space objects reflecting the seed data
'''
def test_get_all_spaces(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    spaces = repository.all()
    assert spaces == [
        Space(1, 'space1', 'description1', '2030-01-01', '2030-02-01', '1000', 1),
        Space(2, 'space2', 'description2', '2031-02-02', '2031-02-28', '15000', 1), 
        Space(3, 'space3', 'description3', '2030-01-15', '2030-02-15', '2000', 2), 
        Space(4, 'space4', 'description4', '2030-03-04', '2030-03-14', '70000', 2)
    ]