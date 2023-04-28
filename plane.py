from vehicle import Vehicle


class Plane(Vehicle):

    def __init__(self, brand, model):
        super().__init__(brand, model)

    def move(self):
        print(f"You can Fly on {self.brand} {self.model}")
