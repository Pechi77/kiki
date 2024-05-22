class Vehicle:
    """
    Represents a delivery vehicle.

    Attributes:
        vehicle_id (str): The vehicle ID.
        max_weight (int): The maximum weight the vehicle can carry in kg.
        speed (int): The speed of the vehicle in km/h.
        available_time (float): The time at which the vehicle will be available for the next delivery.
    """

    def __init__(self, vehicle_id, speed, max_weight):
        """
        Initializes a Vehicle instance.

        Args:
            vehicle_id (str): The vehicle ID.
            speed (int): The speed of the vehicle in km/h.
            max_weight (int): The maximum weight the vehicle can carry in kg.
        """

        self.vehicle_id = vehicle_id
        self.speed = speed
        self.max_weight = max_weight
        self.available_time = 0

    def __repr__(self) -> str:
        return f"Vehicle({self.vehicle_id}, {self.speed}, {self.max_weight}, {self.available_time})"
