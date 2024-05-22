class Offer:
    def __init__(self, code, discount, distance_condition, weight_condition):
        self.code = code
        self.discount = discount
        self.distance_condition = distance_condition
        self.weight_condition = weight_condition

    def is_applicable(self, distance, weight):
        return self.distance_condition(distance) and self.weight_condition(weight)

    def __repr__(self) -> str:
        return f"Offer({self.code}, {self.discount})"
