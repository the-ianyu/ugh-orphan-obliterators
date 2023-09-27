base_price, far_price , increment = 27, 93.5, 0
distance = float(input("Input distance: "))
traffic = float(input("Time in traffic jam (minutes):"))
traffic = round(traffic)
traffic = int(traffic)

distance = distance * 1000
print(f"Distance: {distance}m")

if distance > 9000:
    price = far_price + (((distance // 200) - 45) * 1.3)
elif distance < 9000 and distance > 2199:
    price = base_price + (((distance - 2000) // 200) * 1.9)
elif distance <= 2200:
    price = 27.0
else:
    price = 93.5
    
traffic_money = traffic * 1.5
price = price + traffic_money
print(f"Price: ${price:2f}HKD")
print("")
