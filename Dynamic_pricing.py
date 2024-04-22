def calculate_markup(initial_investment, investment_per_harvest, return_time, harvest_time, product_price, amount_produced_per_harvest):
    # Calculate number of harvests required
    num_harvests_required = return_time / harvest_time
    
    # Calculate total revenue required
    total_revenue_required = num_harvests_required * investment_per_harvest + initial_investment
    
    # Calculate cost of sale
    cost_of_sale = total_revenue_required / (num_harvests_required * amount_produced_per_harvest)
    
    # Calculate markup
    markup = (product_price - cost_of_sale) / cost_of_sale
    
    return markup * 100  # Convert markup to percentage

# Inputs
initial_investment = float(input("Enter initial investment: "))
investment_per_harvest = float(input("Enter investment per harvest: "))
return_time = float(input("Enter time to make returns for seller (in months): "))
harvest_time = float(input("Enter harvest time (in months): "))
product_price = float(input("Enter price of the product: "))
amount_produced_per_harvest = float(input("Enter amount produced per harvest (in kg): "))

# Calculate markup percentage
markup_percentage = calculate_markup(initial_investment, investment_per_harvest, return_time, harvest_time, product_price, amount_produced_per_harvest)
print("Markup Percentage: {:.2f}%".format(markup_percentage))
