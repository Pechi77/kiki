import pytest

from kiki import Offer, Package


@pytest.mark.parametrize(
    "package, expected_output",
    [
        (Package("PKG1", 5, 5, "OFR001"), ("PKG1", 0, 175)),
        (Package("PKG2", 15, 5, "OFR002"), ("PKG2", 0, 275)),
        (Package("PKG3", 10, 100, "OFR003"), ("PKG3", 35, 665)),
    ],
)
def test_delivery_cost_estimation(package, expected_output, base_cost, offers):
    """
    Test to verify that delivery costs and discounts are calculated correctly.
    """

    package.calculate_delivery_cost(base_cost, offers)
    result = (package.pkg_id, round(package.discount), round(package.total_cost))

    assert result == expected_output


@pytest.mark.parametrize(
    "package, expected_output",
    [(Package("PKG4", 10, 100), ("PKG4", 0, 700))],  # When no offer code is provided
)
def test_no_offer_code(package, expected_output, base_cost, offers):
    package.calculate_delivery_cost(base_cost, offers)
    result = (package.pkg_id, round(package.discount), round(package.total_cost))

    assert result == expected_output


@pytest.mark.parametrize(
    "package, expected_output",
    [
        (
            Package("PKG6", 20, 150, "INVALID"),
            ("PKG6", 0, 1050),
        )  # When an invalid offer code is provided
    ],
)
def test_invalid_offer_code(package, expected_output, base_cost, offers):

    package.calculate_delivery_cost(base_cost, offers)
    result = (package.pkg_id, round(package.discount), round(package.total_cost))

    assert result == expected_output
