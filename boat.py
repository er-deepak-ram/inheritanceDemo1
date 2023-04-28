from vehicle import Vehicle


class Boat(Vehicle):

    def __init__(self, brand, model):
        super().__init__(brand, model)

    def move(self):
        print(f"You can Sail on {self.brand} {self.model}")
