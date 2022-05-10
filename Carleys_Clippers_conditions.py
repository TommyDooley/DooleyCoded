hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices:
  total_price += price
print(f"Total price: ${total_price}")

average_price = total_price / len(last_week)
print(f"Average Haircut Price: ${average_price}")

new_prices = [num - 5 for num in prices]
print(f"New list of prices: {new_prices}")

total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print(f"Total Revenue: ${total_revenue}")

average_daily_revenue = total_revenue / 7
print(f"Average Daily Revenue: ${average_daily_revenue}")

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]

print("Haircuts Under $30:")
for cuts in cuts_under_30:
  print(cuts)