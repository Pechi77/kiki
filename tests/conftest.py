import pytest

from kiki import Offer


@pytest.fixture
def offers():
    return {
        "OFR001": Offer("OFR001", 0.10, lambda d: d < 200, lambda w: 70 <= w <= 200),
        "OFR002": Offer(
            "OFR002", 0.07, lambda d: 50 <= d <= 150, lambda w: 100 <= w <= 250
        ),
        "OFR003": Offer(
            "OFR003", 0.05, lambda d: 50 <= d <= 250, lambda w: 10 <= w <= 150
        ),
    }


@pytest.fixture
def base_cost():
    return 100


@pytest.fixture
def max_carriable_weight():
    return 200


@pytest.fixture
def max_speed():
    return 70
