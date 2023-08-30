from lib.booking_repository import *
from lib.booking import *
'''
When I put the connection name in it
it should save the connection
'''

def test_connection(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)
    assert repository.connection == db_connection
'''
When i use #get_all 
I should get all of the bookings
'''

def test_get_all(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)
    bookings = repository.all()
    assert bookings == [
        Booking(1, '2030-01-17', '2030-01-19', 2, 3),
        Booking(2, '2031-02-10', '2031-02-17', 1, 2),
        Booking(3, '2030-03-04', '2030-03-08', 2, 4),
        Booking(4, '2030-01-25', '2030-02-01', 1, 1),
        
        ]