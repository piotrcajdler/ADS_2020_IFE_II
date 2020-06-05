import random
import math

NUMBER_OF_CITIES = 4

def generate_cities(n):
    cities = []
    for i in range(n):
        x = random.randint(-100,100)
        y = random.randint(-100,100)
        cities.append((x, y))
    return cities

def generate_costs(cities,n):

    cities_cost = []
    for element in range(n):
        for sec in range(element+1,n):

                x1 = cities[element][0]
                y1 = cities[element][1]
                x2 = cities[sec][0]
                y2 = cities[sec][1]
                k = math.sqrt(pow((x2-x1),2) + pow((y2-y1),2))
                cities_cost.append((element+1,sec+1,k))
    return cities_cost

k = generate_cities(NUMBER_OF_CITIES)
print(k)

l = generate_costs(k,NUMBER_OF_CITIES)
print(l)