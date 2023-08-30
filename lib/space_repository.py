from lib.space import *

class SpaceRepository:
    def __init__(self, connection) -> None:
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM spaces")
        spaces = []
        for row in rows:
            item = Space(row["id"], row["name"], row["description"], row["start_date"],
                        row["end_date"], row["price"], row["user_id"])
            spaces.append(item)
        return spaces