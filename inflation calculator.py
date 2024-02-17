# Hypothetical historical inflation data for Morocco (replace with actual data)
inflation_data = {
    2000: 1.89,
    2001: 1.40,
    2002: 2.80,
    # Add more years as needed
    2023: 6.66,  # Inflation rate for 2022
}

def calculate_inflation(amount, year):
    # Get the current year
    current_year = 2023  # Replace with the actual current year

    # Calculate the inflated amount for each year
    for yr in range(year, current_year):
        if yr in inflation_data:
            amount += amount * (inflation_data[yr] / 100)

    return amount

# Test the function
amount = float(input("Enter the amount of money: "))
year = int(input("Enter the year: "))
inflated_amount = calculate_inflation(amount, year)

print(f"{amount} dirhams in the year {year} is worth {inflated_amount} dirhams in today's dirhams.")
