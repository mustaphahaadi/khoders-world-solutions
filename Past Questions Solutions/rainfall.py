rainfall = []
total_rainfall = 0

for month in range(12):
    rain = float(input(f"Enter the total rainfall for month {month+1}: "))
    rainfall.append(rain)
    total_rainfall += rain

average_rainfall = total_rainfall/len(rainfall)
maximum_rainfall = max(rainfall)
minimum_rainfall = min(rainfall)

max_month = rainfall.index(maximum_rainfall)+1
min_month = rainfall.index(minimum_rainfall)+1

print(f"Total rainfall for the year is {total_rainfall:.2f}")
print(f"The average monthly rainfall is {average_rainfall:.2f}")
print(f"The maximum rainfall happened in month {max_month} with amount of {maximum_rainfall:.2f}")
print(f"The minimum rainfall happened in month {min_month} with amount of {minimum_rainfall:.2f}")


