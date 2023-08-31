class Space:
    def __init__(self, id, name, description, start_date, end_date, price, user_id) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Space({self.id}, {self.name}, {self.description}, {self.start_date}, {self.end_date}, {self.price}, {self.user_id})"
    


    # [Space(1, space1, description1, 2030-01-01, 2030-02-01, 1000, 1), Space(2, space2, description2, 2031-02-02, 2031-02-28, 15000, 1), Space(3, space3, description3, 2030-01-15, 2030-02-15, 2000, 2), Space(4, space4, description4, 2030-03-04, 2030-03-14, 70000, 2)]
    # [Space(1, space1, description1, 2030-01-01, 2030-02-01, 1000, 1), Space(2, space2, description2, 2031-02-02, 2031-02-28, 15000, 1), Space(3, space3, description3, 2030-01-15, 2030-02-15, 2000, 2), Space(4, space4, description4, 2030-03-04, 2030-03-14, 70000, 2)]