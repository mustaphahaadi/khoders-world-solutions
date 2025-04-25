sales = []
total = 0

for day in range(1,8):
    daily_sale = float(input(f"Enter sales for the day {day}: "))
    sales.append(daily_sale)
    total += daily_sale

print(f"Sales list {sales}")
print(f"The total sales for the week is {total:.2f}")



