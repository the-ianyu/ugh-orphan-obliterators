import re
# to calculate emissions:
#these are kg CO2 per kilometer
small_car_emissions = 0.1386 #(6/100)*2.31
medium_car_emissions = 0.1848 #(8/100)*2.31
large_car_emissions = 0.231 #(10/100)*2.31 large_car_emissions == 7 seater cars

car_type = input("Choose car type (S for small car, M for medium car, L for large car/7 seater car), E for electric car: ")

while car_type.lower() not in ["s", "m", "l", 'e']:
    print("Invalid car type. Please choose again.")
    car_type = input("Choose car type (S for small car, M for medium car, L for large car/7 seater car): ")

if car_type.lower() == "s":
    car_emissions = small_car_emissions
elif car_type.lower() == "m":
    car_emissions = medium_car_emissions
elif car_type.lower() == "e":
    car_emissions = 0
else:
    car_emissions = large_car_emissions
    
while True:
    if car_emissions == 0:
        emission_levels = 0
        break

    distance = input("Input distance travelled: ")
    if re.match("^[0-9.]*$", distance):
        distance = float(distance)
        emission_levels = car_emissions * distance
        emission_levels = round(emission_levels, 2)
        break
    else:
        print("Your input for the distance contains characters outside the range '1234567890'. Please input the distance again.")

if emission_levels == 0:
    print("Congrats! Your journey did not emit any CO2.")
else:   
    print(f"{emission_levels}kg of CO2 were emitted from your journey")





