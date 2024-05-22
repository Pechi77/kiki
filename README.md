# Kiki's Delivery Service CLI

Welcome to Kiki's Delivery Service CLI! This command-line interface allows you to estimate delivery costs with offers and calculate delivery times for packages using a fleet of vehicles.

## Features

1. **Delivery Cost Estimation with Offers**: Calculate the total delivery cost with applicable discounts based on the package weight, distance, and offer code.
2. **Delivery Time Estimation**: Calculate the estimated delivery time for packages using the available fleet of vehicles, considering the maximum weight capacity and speed.

## Requirements

- Python 3.6 or higher

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Pechi77/kiki.git
   ```

2. **Run the application:**

   ```sh
   python -m kiki
   ```

## Usage

When you run the application, you will be prompted to choose one of the two available operations:

1. **Delivery Cost Estimation with Offers**
2. **Delivery Time Estimation**

### Delivery Cost Estimation with Offers

1. **Enter the base delivery cost and the number of packages:**

   ```
   Enter base delivery cost: 100
   Enter number of packages: 3
   ```

2. **Enter the details for each package one by one:**

   ```
   Enter details for packages in this format:
   <PKG> <WEIGHT> <DISTANCE> <OFFER>
   1: PKG1 5 5 OFR001
   2: PKG2 15 5 OFR002
   3: PKG3 10 100 OFR003
   ```

3. **The application will display the total cost for each package with any applicable discounts:**

   ```
   Delivery Cost Estimation Results:
   PKG1 0 175
   PKG2 0 275
   PKG3 35 665
   ```

### Delivery Time Estimation

1. **Enter the base delivery cost and the number of packages:**

   ```
   Enter base delivery cost: 100
   Enter number of packages: 5
   ```

2. **Enter the details for each package one by one:**

   ```
   Enter details for packages in this format:
   <PKG> <WEIGHT> <DISTANCE> <OFFER>
   1: PKG1 50 30 OFR001
   2: PKG2 75 125 OFFR0008
   3: PKG3 175 100 OFFR003
   4: PKG4 110 60 OFFR002
   5: PKG5 155 95 NA
   ```

3. **Enter the number of vehicles, maximum speed, and maximum carriable weight:**

   ```
   Enter vehicle details: <NO_OF_VEHICLES> <MAX_SPEED> <MAX_CARRIABLE_WEIGHT>
   2 70 200
   ```

4. **The application will display the delivery schedule, showing the total cost and estimated delivery time for each package:**

   ```
   Delivery Schedule:
   PKG1 0 750 3.98
   PKG2 0 1475 1.78
   PKG3 0 2350 1.42
   PKG4 105 1395 0.85
   PKG5 0 2125 4.19
   ```
