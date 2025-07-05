write a code to generate 50% profit in python from a stock market curve going up linearly at 10 % from bank and having 5 % variation every 10 days due to volatility gemini periodic 1 month observation commands

import random
import math

# --- CONFIGURATION PARAMETERS ---
INITIAL_INVESTMENT = 1000.0  # Starting capital in USD
TARGET_PROFIT_PERCENTAGE = 50.0 # Desired profit percentage (e.g., 50.0 for 50%)

# Linear upward trend: 10% from the initial bank value per year
# This means the stock's base value increases by 10% of the initial investment annually.
ANNUAL_LINEAR_GROWTH_RATE = 0.10 # 10% of initial investment per year

# Volatility: 5% variation every 10 days
VOLATILITY_PERCENTAGE = 0.05 # 5% variation (e.g., price can go from 0.95x to 1.05x)
VOLATILITY_INTERVAL_DAYS = 10 # Volatility is applied every 10 days

MAX_SIMULATION_DAYS = 365 * 5 # Simulate for a maximum of 5 years to prevent infinite loops

# --- SIMULATION FUNCTIONS ---

def simulate_stock_price(initial_price, days_to_simulate,
                         annual_linear_growth_rate, volatility_percentage, volatility_interval_days):
    """
    Simulates the daily stock price based on linear growth and volatility.

    Args:
        initial_price (float): The starting price of the stock.
        days_to_simulate (int): The total number of days to simulate.
        annual_linear_growth_rate (float): The annual linear growth rate (e.g., 0.10 for 10%).
                                           This is applied as a fixed amount based on initial_price.
        volatility_percentage (float): The percentage of variation due to volatility (e.g., 0.05 for 5%).
        volatility_interval_days (int): The interval in days at which volatility is applied.

    Returns:
        list: A list of daily stock prices.
    """
    stock_prices = [initial_price]
    current_price = initial_price

    # Calculate daily linear growth amount
    # This is the absolute amount added to the base price each day
    daily_linear_growth_amount = (initial_price * annual_linear_growth_rate) / 365.0

    print(f"\n--- Starting Stock Price Simulation ---")
    print(f"Initial Price: ${initial_price:.2f}")
    print(f"Daily Linear Growth Amount: ${daily_linear_growth_amount:.4f}")
    print(f"Volatility: +/- {volatility_percentage*100:.1f}% every {volatility_interval_days} days")

    for day in range(1, days_to_simulate + 1):
        # Apply linear growth
        current_price += daily_linear_growth_amount

        # Apply volatility every 'volatility_interval_days'
        if day % volatility_interval_days == 0:
            # Generate a random factor for volatility (e.g., between 0.95 and 1.05 for 5% variation)
            volatility_factor = random.uniform(1 - volatility_percentage, 1 + volatility_percentage)
            current_price *= volatility_factor
            # Ensure price doesn't drop below a reasonable minimum (e.g., 10% of initial price)
            current_price = max(current_price, initial_price * 0.10)
            # print(f"  Day {day}: Volatility applied. New price: ${current_price:.2f}")

        stock_prices.append(current_price)
    return stock_prices


def calculate_profit_days(initial_investment, target_profit_percentage, stock_prices):
    """
    Calculates the number of days required to achieve the target profit percentage.

    Args:
        initial_investment (float): The initial amount invested.
        target_profit_percentage (float): The desired profit percentage.
        stock_prices (list): A list of daily stock prices from the simulation.

    Returns:
        tuple: (days_to_profit, final_price_at_profit) if profit is achieved,
               or (None, None) if not achieved within the simulation period.
    """
    target_value = initial_investment * (1 + target_profit_percentage / 100.0)
    print(f"\nTarget Profit: {target_profit_percentage:.1f}% (${target_value - initial_investment:.2f})")
    print(f"Target Value to Reach: ${target_value:.2f}")

    for day, price in enumerate(stock_prices):
        if price >= target_value:
            print(f"\n--- Profit Achieved! ---")
            print(f"Achieved {((price - initial_investment) / initial_investment) * 100:.2f}% profit on Day {day}.")
            print(f"Stock Price on Day {day}: ${price:.2f}")
            return day, price
    
    print(f"\n--- Profit Not Achieved ---")
    print(f"Target profit of {target_profit_percentage:.1f}% was not reached within {len(stock_prices)-1} days.")
    print(f"Final stock price: ${stock_prices[-1]:.2f}")
    return None, None


# --- MAIN EXECUTION ---

if __name__ == "__main__":
    print("--- Stock Market Profit Simulation ---")

    # Simulate stock prices
    simulated_prices = simulate_stock_price(
        INITIAL_INVESTMENT,
        MAX_SIMULATION_DAYS,
        ANNUAL_LINEAR_GROWTH_RATE,
        VOLATILITY_PERCENTAGE,
        VOLATILITY_INTERVAL_DAYS
    )

    # Calculate days to achieve profit
    days_to_profit, final_price = calculate_profit_days(
        INITIAL_INVESTMENT,
        TARGET_PROFIT_PERCENTAGE,
        simulated_prices
    )

    if days_to_profit is not None:
        print(f"\nSummary:")
        print(f"Initial Investment: ${INITIAL_INVESTMENT:.2f}")
        print(f"Target Profit: {TARGET_PROFIT_PERCENTAGE:.1f}%")
        print(f"Profit Achieved on Day: {days_to_profit}")
        print(f"Stock Value at Profit: ${final_price:.2f}")
        print(f"Total Profit: ${final_price - INITIAL_INVESTMENT:.2f}")
    else:
        print(f"\nSummary:")
        print(f"Initial Investment: ${INITIAL_INVESTMENT:.2f}")
        print(f"Target Profit: {TARGET_PROFIT_PERCENTAGE:.1f}%")
        print(f"Profit not achieved within {MAX_SIMULATION_DAYS} days.")
        print(f"Final Stock Value: ${simulated_prices[-1]:.2f}")
