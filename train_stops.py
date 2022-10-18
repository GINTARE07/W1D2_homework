stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]
print(stops)
stops.append("Edinburgh Wawerley")
print(stops)
a="Glasgow Queen St"
stops.insert(0, a)
print(stops)
b= "Polmont"
stops.insert(2, b)
print(stops)
Linlithgow = 3
print(3)
stops.remove("Livingston")
print(stops)
stops.pop(1)
num_of_stops=stops
len(stops)
print(stops)
sort_stops = sorted (stops)
print(sort_stops)
sort_stops = sorted(stops, reverse = True)
print(sort_stops)

stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]
for stop in stops: 
    print(stop)
