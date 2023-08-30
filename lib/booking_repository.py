from lib.booking import Booking
class BookingRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute("SELECT * FROM bookings")
        bookings = []
        for row in rows:
            booking = Booking(row["id"], row["start_date"], row["end_date"], row["user_id"], row["space_id"])
            bookings.append(booking)
        return bookings
    