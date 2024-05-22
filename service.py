import math
from itertools import combinations

from kiki import Vehicle, Offer, Package


def estimate_delivery_cost(base_cost, packages):
    """
    Estimates the delivery cost for each package and applies any applicable discounts.

    Args:
        base_cost (int): The base cost of delivery.
        packages (list of Package): The list of packages to estimate delivery costs for.
    """

    offers = {
        "OFR001": Offer("OFR001", 0.10, lambda d: d < 200, lambda w: 70 <= w <= 200),
        "OFR002": Offer(
            "OFR002", 0.07, lambda d: 50 <= d <= 150, lambda w: 100 <= w <= 250
        ),
        "OFR003": Offer(
            "OFR003", 0.05, lambda d: 50 <= d <= 250, lambda w: 10 <= w <= 150
        ),
    }

    results = []

    for package in packages:
        package.calculate_delivery_cost(base_cost, offers)
        results.append(
            (package.pkg_id, round(package.discount), round(package.total_cost))
        )

    return results


def find_optimal_load(packages, max_weight):
    """
    Finds the optimal combination of packages that maximizes the number of packages
    without exceeding the maximum weight capacity. In case of ties in weight,
    it selects the combination with the smallest maximum distance.

    Args:
        packages (list of Package): The list of packages to choose from.
        max_weight (int): The maximum weight capacity of the vehicle.

    Returns:
        list of Package: The optimal combination of packages.
    """
    best_combination = []
    best_weight = 0
    best_max_distance = float("inf")

    for r in range(1, len(packages) + 1):
        for combo in combinations(packages, r):
            total_weight = sum(pkg.weight for pkg in combo)
            max_distance = max(pkg.distance for pkg in combo)

            if total_weight <= max_weight:
                if len(combo) > len(best_combination):
                    best_combination = combo
                    best_weight = total_weight
                    best_max_distance = max_distance
                elif len(combo) == len(best_combination):
                    if total_weight > best_weight:
                        best_combination = combo
                        best_weight = total_weight
                        best_max_distance = max_distance
                    elif (
                        total_weight == best_weight and max_distance < best_max_distance
                    ):
                        best_combination = combo
                        best_weight = total_weight
                        best_max_distance = max_distance

    return best_combination


def load_vehicles(packages, vehicles):
    """
    Loads vehicles with the optimal set of packages and calculates the delivery times.

    Args:
        packages (list of Package): The list of packages to be delivered.
        vehicles (list of Vehicle): The list of available vehicles.

    Returns:
        list of tuple: A list of tuples with package ID, discount, total cost, and delivery time.
    """

    delivery_schedule = []
    time_elapsed = 0

    while packages:
        vehicles.sort(key=lambda v: v.available_time)
        vehicle = vehicles[0]
        optimal_load = find_optimal_load(packages, vehicle.max_weight)
        print(f"optimal_load: {optimal_load}")
        if not optimal_load:
            break

        max_distance = max(pkg.distance for pkg in optimal_load)
        delivery_time = max_distance / vehicle.speed
        delivery_time = math.floor(delivery_time * 100) / 100
        vehicle.available_time += 2 * delivery_time

        for pkg in optimal_load:
            pkg_delivery_time = pkg.calculate_delivery_time(vehicle.speed)
            pkg.delivery_time = time_elapsed + pkg_delivery_time
            delivery_schedule.append(
                (
                    pkg.pkg_id,
                    round(pkg.discount),
                    round(pkg.total_cost),
                    round(pkg.delivery_time, 2),
                )
            )
            packages.remove(pkg)

        time_elapsed = min(vehicle.available_time for vehicle in vehicles)
    delivery_schedule = sorted(delivery_schedule, key=lambda x: x[0])
    return delivery_schedule


def simulate_delivery(
    base_cost, packages, num_vehicles, max_speed, max_carriable_weight
):
    """
    Simulates the delivery process, estimating delivery costs and calculating delivery times.

    Args:
        base_cost (int): The base cost of delivery.
        packages (list of Package): The list of packages to be delivered.
        num_vehicles (int): The number of available vehicles.
        max_speed (int): The maximum speed of the vehicles.
        max_carriable_weight (int): The maximum weight capacity of the vehicles.

    Returns:
        list of tuple: A list of tuples with package ID, discount, total cost, and delivery time.
    """

    vehicles = [
        Vehicle(f"V{i+1}", max_speed, max_carriable_weight) for i in range(num_vehicles)
    ]
    estimate_delivery_cost(base_cost, packages)
    delivery_schedule = load_vehicles(packages, vehicles)
    return delivery_schedule
