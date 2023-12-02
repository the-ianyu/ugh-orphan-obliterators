import googlemaps
import os

here = os.path.dirname(os.path.realpath(__file__))
filepath = os.path.join(here, "api-key.txt")

with open(filepath, "r") as f:
    key = f.read()

gmaps = googlemaps.Client(key=key)
i1 = input("Enter the starting point: ")
i2 = input("Enter the destination: ")
directions_result = gmaps.directions(i1, i2, mode="driving", departure_time="now")

if len(directions_result) == 0:
    print("No route found")
else:
    print("Time required: " + directions_result[0]["legs"][0]["duration"]["text"])
    print("Distance: " + directions_result[0]["legs"][0]["distance"]["text"])
    print("Traffic delay: " + directions_result[0]["legs"][0]["duration_in_traffic"]["text"])
