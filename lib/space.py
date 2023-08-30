class Space:
    def __init__(self, id, name, description, start_date, end_date, price, user_id) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.user_id = user_id

    def __eq__(self, other) -> bool:
        return self.__dict__ == other.__dict__