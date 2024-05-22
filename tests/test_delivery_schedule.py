import pytest

from kiki import Offer, Package, Vehicle
from kiki.service import simulate_delivery


def test_delivery_simulation(base_cost, max_carriable_weight, max_speed):
    """
    Test to verify that the delivery simulation correctly assigns packages to vehicles
    and calculates delivery times.
    """
    packages = [
        Package("PKG1", 50, 30, "OFR001"),
        Package("PKG2", 75, 125, "OFR002"),
        Package("PKG3", 175, 100, "OFR003"),
        Package("PKG4", 110, 60, "OFR002"),
        Package("PKG5", 155, 95, None),
    ]
    num_vehicles = 2

    expected_schedule = [
        ("PKG1", 0, 750, 3.98),
        ("PKG2", 0, 1475, 1.78),
        ("PKG3", 0, 2350, 1.42),
        ("PKG4", 105, 1395, 0.85),
        ("PKG5", 0, 2125, 4.19),
    ]

    result = simulate_delivery(
        base_cost, packages, num_vehicles, max_speed, max_carriable_weight
    )

    assert result == expected_schedule


def test_packages_with_maximum_weight_and_less_distance_picked_first(
    base_cost, max_carriable_weight, max_speed
):
    """
    Test to verify that packages with the same weight are picked first based on less distance.

    """
    packages = [
        Package("PKG1", 200, 30, "OFR001"),
        Package("PKG2", 200, 50, "OFR002"),
        Package("PKG3", 200, 10, "OFR003"),
    ]
    num_vehicles = 1

    expected_schedule = [
        ("PKG1", 225, 2025, 0.7),
        ("PKG2", 165, 2186, 1.83),
        ("PKG3", 0, 2150, 0.14),
    ]

    result = simulate_delivery(
        base_cost, packages, num_vehicles, max_speed, max_carriable_weight
    )
    assert result == expected_schedule
