import math


class Package:
    """
    Represents a package to be delivered.

    Attributes:
        pkg_id (str): The package ID.
        weight (int): The weight of the package in kg.
        distance (int): The distance to the delivery destination in km.
        offer_code (str, optional): The offer code applied to the package.
        discount (float): The discount amount applied to the package.
        total_cost (float): The total delivery cost after applying the discount.
        delivery_time (float): The estimated delivery time in hours.
    """

    def __init__(self, pkg_id, weight, distance, offer_code=None):
        """
        Initializes a Package instance.

        Args:
            pkg_id (str): The package ID.
            weight (int): The weight of the package in kg.
            distance (int): The distance to the delivery destination in km.
            offer_code (str, optional): The offer code applied to the package.
        """

        self.pkg_id = pkg_id
        self.weight = weight
        self.distance = distance
        self.offer_code = offer_code
        self.discount = 0
        self.total_cost = 0
        self.delivery_time = 0

    def calculate_delivery_cost(self, base_cost, offers):
        """
        Calculates the delivery cost and applies any applicable discounts.

        Args:
            base_cost (int): The base cost of delivery.
            offers (dict): A dictionary of available offers.

        Returns:
            float: The total delivery cost after applying the discount.
        """

        delivery_cost = base_cost + (self.weight * 10) + (self.distance * 5)        
        offer = offers.get(self.offer_code)
        if offer and offer.is_applicable(self.distance, self.weight):
            self.discount = delivery_cost * offer.discount
        self.total_cost = delivery_cost - self.discount
        return self.total_cost

    def calculate_delivery_time(self, speed):
        """
        Calculates the delivery time based on the vehicle speed.

        Args:
            speed (int): The speed of the vehicle in km/h.

        Returns:
            float: The estimated delivery time in hours.
        """

        delivery_time = self.distance / speed
        return math.floor(delivery_time * 100) / 100

    def __repr__(self) -> str:
        return (
            f"Package({self.pkg_id}, {self.weight}, {self.distance}, {self.offer_code})"
        )
