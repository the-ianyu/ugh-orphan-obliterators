from pandas import DataFrame
import googlemaps
import os

here = os.path.dirname(os.path.realpath(__file__))
filepath = os.path.join(here, "api-key.txt")

with open(filepath, "r") as f:
    key = f.read()

gmaps = googlemaps.Client(key=key)
start = input("Enter the starting point: ")
end = input("Enter the destination: ")
cartype = input("Enter the car type (small, medium, large): ")
cartype = cartype[0].lower()
directions_result = gmaps.directions(start, end, mode="driving", alternatives=True)

emissions_ratio = {
    "s": 0.1386, #(6/100)*2.31
    "m": 0.1848, #(8/100)*2.31
    "l": 0.231, #(10/100)*2.31
}

template = {
    "duration": float("inf"),
    "distance": float("inf"),
    "emissions": float("inf"),
    "summary": "N/A"
}

best_routes = {
    "Best Route": template.copy(),
    "Quickest Route": template.copy(),
    "Shortest Route": template.copy(),
    "Env. Friendly Route": template.copy(),
}

if len(directions_result) == 0: # Catch for no route found
    print("No route found")
else:
    # Finding the overall best route
    for key in template.keys():
        if key == "emissions":
            best_routes["Best Route"][key] = round(emissions_ratio[cartype] * directions_result[0]["legs"][0]["distance"]["value"]/1000, 2)
            continue
        elif key == "summary":
            best_routes["Best Route"][key] = "N/A"#directions_result[0]["summary"]
            continue
        best_routes["Best Route"][key] = directions_result[0]["legs"][0][key]["value"]
    
    # Finding best routes for all other aspects
    for route in directions_result:
        route["legs"][0]["emissions"] = {"value": round(emissions_ratio[cartype] * route["legs"][0]["distance"]["value"]/1000, 2)}
        route["legs"][0]["summary"] = {"value": "N/A"}#route["summary"]}
        for a, b in zip(list(template.keys())[:-1], list(best_routes.keys())[1:]):  
            if route["legs"][0][a]["value"] < best_routes[b][a]:
                for key in template.keys():
                    best_routes[b][key] = route["legs"][0][key]["value"]
    
    # Formatting for output
    for key in best_routes.keys():
        best_routes[key] = [best_routes[key][aspect] for aspect in template.keys()]
    print()
    print(DataFrame(best_routes, index=[x.title() for x in template.keys()]))
