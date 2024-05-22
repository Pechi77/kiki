import argparse
import sys
from kiki.service import simulate_delivery, estimate_delivery_cost
from kiki import Package


def get_package_input(no_of_packages):
    """
    Function to interactively get package input from the user.

    Args:
        no_of_packages (int): The number of packages to input.

    Returns:
        list of Package: A list of Package objects.
    """
    packages = []
    print(
        f"Enter details for packages in this format:\n <PKG> <WEIGHT> <DISTANCE> <OFFER>"
    )
    for i in range(no_of_packages):

        try:
            package_info = input(f"{i+1}: ").strip().split()
            if len(package_info) == 3:
                package_info.append(None)
            if len(package_info) != 4:
                raise ValueError
            pkg_id, pkg_weight, pkg_distance, offer_code = package_info
            pkg_weight = int(pkg_weight)
            pkg_distance = int(pkg_distance)
            packages.append(Package(pkg_id, pkg_weight, pkg_distance, offer_code))
        except ValueError:
            print("Invalid input. Please enter the details again.")
            return get_package_input(no_of_packages)
        except KeyboardInterrupt:
            print("\nInput process interrupted by user. Exiting.")
            sys.exit()
    return packages


def delivery_cost_estimation():
    """
    Function to perform Delivery Cost Estimation with Offers.
    """
    print("Delivery Cost Estimation with Offers:")

    try:
        base_delivery_cost = int(input("Enter base delivery cost: "))
        no_of_packages = int(input("Enter number of packages: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    print("Enter package details:")
    packages = get_package_input(no_of_packages)

    estimate_delivery_cost(base_delivery_cost, packages)

    print("\nDelivery Cost Estimation Results:")
    for pkg in packages:
        print(f"{pkg.pkg_id} {pkg.discount} {pkg.total_cost}")


def delivery_time_estimation():
    """
    Function to perform Delivery Time Estimation.
    """
    print("Delivery Time Estimation:")

    try:
        base_delivery_cost = int(input("Enter base delivery cost: "))
        no_of_packages = int(input("Enter number of packages: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    packages = get_package_input(no_of_packages)
    print(
        "Enter vehicle details: <NO_OF_VEHICLES> <MAX_SPEED> <MAX_CARRIABLE_WEIGHT>\n"
    )
    try:

        vehicle_info = input().strip().split()
        if len(vehicle_info) != 3:
            print("Invalid input. Please enter the details again.")
            sys.exit(1)
        no_of_vehicles, max_speed, max_carriable_weight = map(int, vehicle_info)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    result = simulate_delivery(
        base_delivery_cost, packages, no_of_vehicles, max_speed, max_carriable_weight
    )

    print("\nDelivery Schedule:")
    for pkg_id, discount, total_cost, delivery_time in result:
        print(f"{pkg_id} {discount} {total_cost} {delivery_time:.2f}")


def main():
    print("Welcome to the Delivery Cost and Time Estimation CLI!")
    print("Choose an operation to perform:")
    print("1. Delivery Cost Estimation with Offers")
    print("2. Delivery Time Estimation")

    try:
        choice = int(input("Enter the number of your choice: "))
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")
        return

    if choice == 1:
        delivery_cost_estimation()
    elif choice == 2:
        delivery_time_estimation()
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
    sys.exit(1)
