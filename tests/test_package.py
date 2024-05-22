import pytest
from kiki import Package
from kiki import Offer


def test_calculate_delivery_cost():
    """
    Test the calculate_delivery_cost method of the Package class.
    """
    offers = {
        "OFR001": Offer("OFR001", 0.10, lambda d: d < 200, lambda w: 70 <= w <= 200),
    }
    pkg = Package("PKG1", 50, 30, "OFR001")
    base_cost = 100
    total_cost = pkg.calculate_delivery_cost(base_cost, offers)
    assert total_cost == 750  
    assert pkg.discount == 0  
    assert pkg.total_cost == 750

    pkg = Package("PKG2", 100, 30, "OFR001")
    total_cost = pkg.calculate_delivery_cost(base_cost, offers)
    assert pkg.discount == 125 
    assert pkg.total_cost == 1125

def test_calculate_delivery_time():
    """
    Test the calculate_delivery_time method of the Package class.
    """
    pkg = Package("PKG1", 50, 30, "OFR001")
    delivery_time = pkg.calculate_delivery_time(60)
    assert delivery_time == 0.5  # 30 / 60 = 0.5
    assert pkg.calculate_delivery_time(30) == 1  # 30 / 30 = 1
