from lib.space_repository import *
from lib.space import *
import datetime

'''
When we call SpaceRepository #all method
We get a list of Space objects reflecting the seed data
'''
def test_get_all_spaces(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    spaces = repository.all()
    assert spaces == [
        Space(1, 'space1', 'description1', datetime.date(2030,1,1), datetime.date(2030,2,1), 1000, 1),
        Space(2, 'space2', 'description2', datetime.date(2031,2,2), datetime.date(2031,2,28), 15000, 1), 
        Space(3, 'space3', 'description3', datetime.date(2030,1,15), datetime.date(2030,2,15), 2000, 2), 
        Space(4, 'space4', 'description4', datetime.date(2030,3,4), datetime.date(2030,3,14), 70000, 2)
    ]
